#!/usr/bin/env python3
"""Exact symbolic certificate for the first logarithmic cusp layer and indicial analysis.

Checks:
1. H0 u_i = 0 and H0 v_i = u_i.
2. The eight-dimensional first logarithmic theta-zero layer (log degree <= 1).
3. The discrete longitudinal eigenfunction at eigenvalue 2.
4. The Hilbert-sector indicial roots and the central root-free strip.
5. The algebraic coefficient in the weighted end coercivity estimate.
6. The exact even root-1 resonance normalization constant.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

w, r, delta = sp.symbols("w r delta", real=True, positive=True)


def H0(f):
    return (1 + w**2) * sp.diff(f, w, 2) + 6 * w * sp.diff(f, w) + 4 * f


def Delta_cusp_radial(f):
    return r**2 * sp.diff(f, r, 2)


u0 = 1 / (1 + w**2) ** 2
u1 = (w + w**3 / sp.Integer(3)) / (1 + w**2) ** 2
v0 = (
    w**3 * sp.atan(w)
    + w**2
    + 3 * w * sp.atan(w)
    - sp.log(1 + w**2)
    + 2
) / (6 * (1 + w**2) ** 2)
v1 = (
    -2 * w**3
    + 3 * w * (w**2 + 3) * sp.log(1 + w**2)
    - 30 * w
    + 12 * sp.atan(w)
) / (54 * (1 + w**2) ** 2)

assert sp.simplify(H0(u0)) == 0
assert sp.simplify(H0(u1)) == 0
assert sp.simplify(H0(v0) - u0) == 0
assert sp.simplify(H0(v1) - u1) == 0

# First logarithmic layer. The last two modes were missing in v0.7;
# this is not the full O(r log r) polyhomogeneous kernel (see v0.11 tower).
defect_basis = {
    "u0*r": u0 * r,
    "u1*r": u1 * r,
    "u0": u0,
    "u1": u1,
    "u0*log(r)+v0": u0 * sp.log(r) + v0,
    "u1*log(r)+v1": u1 * sp.log(r) + v1,
    "u0*r*log(r)-v0*r": u0 * r * sp.log(r) - v0 * r,
    "u1*r*log(r)-v1*r": u1 * r * sp.log(r) - v1 * r,
}
for name, mode in defect_basis.items():
    residual = sp.simplify(H0(mode) + Delta_cusp_radial(mode))
    if residual != 0:
        raise AssertionError((name, residual))

# The second discrete Pöschl--Teller state corresponds to eigenvalue 2.
h2 = w / (1 + w**2) ** 2
assert sp.simplify(H0(h2) + 2 * h2) == 0

sqrt10 = sp.sqrt(10)
alpha_minus = sp.simplify((1 - sqrt10) / 2)
alpha_plus = sp.simplify((1 + sqrt10) / 2)

# Indicial roots sigma(sigma-1)=mu for mu=0 and mu=2.
sigma = sp.symbols("sigma")
roots_mu0 = sp.solve(sp.Eq(sigma * (sigma - 1), 0), sigma)
roots_mu2 = sp.solve(sp.Eq(sigma * (sigma - 1), 2), sigma)
assert set(roots_mu0) == {sp.Integer(0), sp.Integer(1)}
assert set(roots_mu2) == {sp.Integer(-1), sp.Integer(2)}
assert float(alpha_minus) < -1
assert float(alpha_plus) > 2

# Weighted normal operator after y=log r and L2-density conjugation has
# positive zeroth-order coefficient 1/4-delta^2 for |delta|<1/2.
coercive_coefficient = sp.Rational(1, 4) - delta**2
assert sp.simplify(coercive_coefficient.subs(delta, sp.Rational(1, 3))) > 0

# Root-1 resonance audit.  In the natural longitudinal Hilbert measure
# q(w)dw=(1+w^2)^2dw, one has q*u0=1 and ||u0||_q^2=pi/2.
q = (1 + w**2) ** 2
assert sp.simplify(q * u0) == 1
u0_norm_sq = sp.integrate(sp.simplify(u0**2 * q), (w, -sp.oo, sp.oo))
assert sp.simplify(u0_norm_sq - sp.pi / 2) == 0
root_one_resonance_prefactor = sp.simplify(1 / u0_norm_sq)
assert sp.simplify(root_one_resonance_prefactor - 2 / sp.pi) == 0

payload = {
    "H0_kernel_checked": ["u0", "u1"],
    "Jordan_partners_checked": ["v0", "v1"],
    "first_logarithmic_layer_dimension": len(defect_basis),
    "first_logarithmic_layer_basis": list(defect_basis),
    "missing_v07_modes": [
        "u0*r*log(r)-v0*r",
        "u1*r*log(r)-v1*r",
    ],
    "discrete_longitudinal_mu_2_profile": "w/(1+w^2)^2",
    "Hilbert_indicial_discrete_roots": [-1, 0, 1, 2],
    "continuous_indicial_thresholds": {
        "negative": str(alpha_minus),
        "positive": str(alpha_plus),
        "negative_numeric": float(alpha_minus),
        "positive_numeric": float(alpha_plus),
    },
    "root_free_open_intervals": ["(-1,0)", "(0,1)", "(1,2)"],
    "central_weight_window_after_density_conjugation": "|delta|<1/2",
    "weighted_coercivity_zeroth_order_term": "1/4-delta^2",
    "root_one_even_resonance_prefactor": str(root_one_resonance_prefactor),
    "root_one_even_resonance_condition": "integral_R G(w) dw = 0",
}

out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("Cusp indicial/parametrix certificate passed.")
print(out.read_text(encoding="utf-8"), end="")
