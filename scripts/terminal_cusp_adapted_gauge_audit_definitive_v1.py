#!/usr/bin/env python3
"""Finite diagnostic for the terminal-cusp adapted gauge bookkeeping.

This script does not prove the analytic estimates.  It checks:
(1) a finite order-zero tame-frame family on three cusps;
(2) failure of a fixed non-adapted positive-order gauge in the fast-cusp regime;
(3) near-identity of the adapted radial coframe block when the approached order is zero.
"""
from __future__ import annotations
import json, math
from pathlib import Path

cusps = [0, 1, 2]
frames = {}
for k in cusps:
    ell = (k + 1) % 3
    orders = [0, 0, 0]
    orders[ell] = 1
    assert orders[k] == 0
    assert sum(orders) == 1
    frames[str(k)] = {"approached_cusp": k, "orders": orders}

samples = []
for R in [20.0, 40.0, 80.0]:
    for s in [0.2, 0.5, 0.8]:
        S_alg = math.exp(s * R)
        T = math.exp(R)
        # Fixed positive-order gauge: S_alg = S_g + T (bounded unit omitted).
        S_g_fixed = S_alg - T
        fixed_fails_positive_depth = S_g_fixed <= 0.0

        # Cusp-adapted order a_k=0; use a bounded unit term b=1.
        b = 1.0
        S_g_adapted = S_alg - b
        det_alg_from_gauge = S_g_adapted / S_alg
        offdiag = 0.0
        error = abs(det_alg_from_gauge - 1.0)
        samples.append({
            "R": R,
            "s": s,
            "T_over_S_alg": T / S_alg,
            "fixed_positive_order_depth": S_g_fixed,
            "fixed_positive_order_fails": fixed_fails_positive_depth,
            "adapted_determinant": det_alg_from_gauge,
            "adapted_offdiag": offdiag,
            "adapted_error": error,
        })
        assert fixed_fails_positive_depth
        assert 0.0 < det_alg_from_gauge <= 1.0
        assert error <= 2.0 / S_alg

result = {
    "status": "PASS",
    "purpose": "finite bookkeeping and formula diagnostic only",
    "cusp_adapted_frame_family": frames,
    "sample_count": len(samples),
    "samples": samples,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2), encoding='utf-8')
print("PASS")
print(f"frames={len(frames)} samples={len(samples)}")
print(out)
