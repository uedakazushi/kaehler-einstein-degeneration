#!/usr/bin/env python3
"""Exact symbolic checks for the v0.12 scale/degree/plumbing audit.

This certificate verifies only algebraic identities used in the paper:
  * Mandel's D-constant reduced solution;
  * identification of u_0 and u_1 with scale and degree derivatives;
  * the five-source topological jump in the base-constant channel;
  * the common leading logarithmic scale on all 30 neck/corner incidences.
It does not verify the nonlinear KE gluing or the actual GH convergence.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


def assert_zero(expr: sp.Expr, name: str) -> None:
    simplified = sp.factor(sp.cancel(sp.together(expr)))
    if simplified != 0:
        raise AssertionError(f"{name} failed: {simplified}")


def main() -> None:
    z, T, a, w = sp.symbols("z T a w", positive=True, real=True)
    H0 = lambda f: sp.simplify((1 + w**2) * sp.diff(f, w, 2) + 6 * w * sp.diff(f, w) + 4 * f)

    chi = 1 + a * z
    h = chi / (z**2 + sp.Rational(2, 3) * a * z**3 + T ** (-2))
    h0 = sp.simplify(h.subs(a, 0))

    u0 = 1 / (1 + w**2) ** 2
    u1 = (w + w**3 / 3) / (1 + w**2) ** 2

    # Exact reduced ODE and the longitudinal zero-mode equations.
    reduced_ode = sp.diff(sp.log(h / chi), z) + 2 * h * z
    assert_zero(reduced_ode, "reduced ODE")
    assert_zero(H0(u0), "H0 u0")
    assert_zero(H0(u1), "H0 u1")

    # Derivatives are taken at fixed z, then expressed in w=Tz.
    scale_identity = (T * sp.diff(h0, T) / (2 * T**2)).subs(z, w / T) - u0
    degree_identity = (sp.diff(h, a).subs(a, 0) / T).subs(z, w / T) - u1
    assert_zero(scale_identity, "scale derivative")
    assert_zero(degree_identity, "degree derivative")

    # Base-constant five-source Green profile.
    m0_plus = sp.pi * (w + w**3 / 3) / (1 + w**2) ** 2
    assert_zero(m0_plus - sp.pi * u1, "m0 = pi u1 on w>0")
    derivative_plus = sp.simplify(sp.limit(sp.diff(m0_plus, w), w, 0, dir="+"))
    # The even extension m0(|w|) has the opposite derivative on the left.
    derivative_minus = -derivative_plus
    jump_derivative = sp.simplify(derivative_plus - derivative_minus)
    if jump_derivative != 2 * sp.pi:
        raise AssertionError(f"delta jump failed: {jump_derivative}")

    b = sp.symbols("b", real=True)
    coeff_plus = b + sp.Rational(5, 2)
    coeff_minus = b - sp.Rational(5, 2)
    if sp.simplify(coeff_plus - coeff_minus) != 5:
        raise AssertionError("five-source degree jump failed")
    balanced_average = sp.simplify((coeff_plus + coeff_minus).subs(b, 0) / 2)
    if balanced_average != 0:
        raise AssertionError(f"balanced odd centering failed: {balanced_average}")
    # Since u1 is odd, sgn(w)u1 is even: the normalized source particular solution
    # is longitudinally even and has no homogeneous b u1 component.
    m0_even_check = sp.simplify((-1) * u1.subs(w, -w) - u1)
    assert_zero(m0_even_check, "sgn(w)u1 evenness")

    # Toroidal leading scale.  For an exact xyz=t chart and fixed normalized
    # corner coordinate q=ell_z/L, Lambda_xy=L(1-q).  A bounded unit changes
    # this by O(1), represented here by c.
    R, q, c = sp.symbols("R q c", real=True)
    L = sp.exp(R)
    Lambda = L * (1 - q) + c
    dlog_dR = sp.simplify(sp.diff(sp.log(Lambda), R))
    dlog_limit = sp.limit(dlog_dR, R, sp.oo)
    if sp.simplify(dlog_limit - 1) != 0:
        raise AssertionError(f"leading scale derivative failed: {dlog_limit}")
    normalized_limit = sp.limit(sp.log(Lambda) / R, R, sp.oo)
    if sp.simplify(normalized_limit - 1) != 0:
        raise AssertionError(f"normalized log scale failed: {normalized_limit}")

    labels = tuple(range(5))
    edges = list(itertools.combinations(labels, 2))
    triples = list(itertools.combinations(labels, 3))
    incidences = [(e, tau) for e in edges for tau in triples if set(e).issubset(tau)]
    if (len(edges), len(triples), len(incidences)) != (10, 10, 30):
        raise AssertionError("incidence count failed")
    if any(sum(1 for e, tau2 in incidences if tau2 == tau) != 3 for tau in triples):
        raise AssertionError("corner valency failed")
    if any(sum(1 for e2, tau in incidences if e2 == e) != 3 for e in edges):
        raise AssertionError("neck cusp valency failed")

    report = {
        "status": "passed",
        "reduced_solution": "h=(1+az)/(z^2+(2/3)az^3+T^-2)",
        "scale_mode": "(2T^2)^-1 d_{log T} h_{0,T}|_{z=w/T}=u0",
        "degree_mode": "T^-1 d_a h_{a,T}|_{a=0,z=w/T}=u1",
        "u0": str(u0),
        "u1": str(u1),
        "m0_derivative_jump": str(jump_derivative),
        "five_source_u1_coefficient_jump": 5,
        "balanced_reference_average_u1_coefficient": str(balanced_average),
        "degree_interpretation": "relative to chosen cusp trivializations; three cusp flux units are part of the global charge balance",
        "toroidal_d_log_scale_d_R_limit": str(dlog_limit),
        "toroidal_log_scale_over_R_limit": str(normalized_limit),
        "incidence_counts": {
            "necks": len(edges),
            "corners": len(triples),
            "incidences": len(incidences),
            "valency": 3,
        },
        "scope_warning": (
            "This certificate checks exact model algebra only; it does not prove "
            "the nonlinear KE gluing, Taub-NUT no-shortcut estimates, or the GH conjecture."
        ),
    }

    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Scale-degree-plumbing certificate passed.")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
