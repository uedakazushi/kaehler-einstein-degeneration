#!/usr/bin/env python3
"""Diagnostic audit for the slow-box frame-shear formulas in Paper I, Part II (definitive v1).

This script is not a proof.  It verifies the exact radial/angular coframe
identities symbolically and samples the conditioning of the resulting
2-by-2 shear block in the regime B+Lambda=o(A).
"""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

try:
    import sympy as sp
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"sympy is required: {exc}")

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "slow_box_frame_shear_audit_definitive_v1.json"
OUT_TXT = HERE / "SLOW_BOX_FRAME_SHEAR_AUDIT_RUN_definitive_v1.txt"

# Symbolic identities: Shat = S + a*T + b.
S, T, a, b = sp.symbols("S T a b", positive=True, finite=True)
dS, dT, db = sp.symbols("dS dT db")
Shat = S + a*T + b
lhs_rad = (dS + a*dT + db) / Shat
rhs_rad = (S/Shat)*(dS/S) + (a*T/Shat)*(dT/T) + db/Shat
radial_identity = sp.simplify(lhs_rad - rhs_rad) == 0

# Angular identity in the unit covectors eta_v=dtheta_v/S, eta_z=dtheta_z/T.
dth_v, dth_z, dargu = sp.symbols("dth_v dth_z dargu")
lhs_ang = (dth_v + a*dth_z + dargu) / Shat
rhs_ang = (S/Shat)*(dth_v/S) + (a*T/Shat)*(dth_z/T) + dargu/Shat
angular_identity = sp.simplify(lhs_ang - rhs_ang) == 0

rng = random.Random(20260830)
max_cond = 0.0
max_error = 0.0
samples = 20000
violations = 0
for _ in range(samples):
    A = rng.uniform(20.0, 120.0)
    # Force B+Lambda <= 0.22 A, a quantitative slow-box regime.
    BL = rng.uniform(0.0, 0.22*A)
    Sval = math.exp(A - rng.uniform(0.0, 0.1*A))
    Tval = math.exp(BL)
    aval = rng.choice([-2, -1, 0, 1, 2])
    bval = rng.uniform(-2.0, 2.0)
    Sh = Sval + aval*Tval + bval
    if Sh <= 0:
        violations += 1
        continue
    alpha = Sval / Sh
    beta = aval*Tval / Sh
    # Radial/angle shear block on (normal,residual) unit coframes.
    # [[alpha,beta],[0,1]].
    tr = alpha*alpha + beta*beta + 1.0
    det2 = alpha*alpha
    disc = max(0.0, tr*tr - 4.0*det2)
    smax2 = 0.5*(tr + math.sqrt(disc))
    smin2 = 0.5*(tr - math.sqrt(disc))
    cond = math.sqrt(smax2 / smin2)
    err = math.sqrt((alpha-1.0)**2 + beta**2)
    max_cond = max(max_cond, cond)
    max_error = max(max_error, err)
    # A coarse theoretical envelope in this sampled regime.
    envelope = 20.0*math.exp(-0.65*A)
    if A >= 40.0 and err > envelope:
        # The random S lower bound allows a 0.1A loss and BL a 0.22A gain,
        # so exponent -0.65A is conservative.
        violations += 1

result = {
    "version": "definitive-v1",
    "radial_identity": radial_identity,
    "angular_identity": angular_identity,
    "samples": samples,
    "max_condition_number": max_cond,
    "max_frobenius_error_from_identity": max_error,
    "violations": violations,
    "status": "PASS" if radial_identity and angular_identity and violations == 0 else "FAIL",
    "note": "Diagnostic only; analytic derivative estimates are proved in Part II.",
}
OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
OUT_TXT.write_text(
    "Slow-box frame-shear diagnostic definitive v1\n"
    "==================================\n"
    + "\n".join(f"{k}: {v}" for k, v in result.items())
    + "\n",
    encoding="utf-8",
)
print(json.dumps(result, indent=2, sort_keys=True))
