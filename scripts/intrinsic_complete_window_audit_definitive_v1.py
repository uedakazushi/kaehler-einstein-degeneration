#!/usr/bin/env python3
"""Numerical audit for the intrinsic complete-window formulae in Paper I, Part I (definitive v1).

This is a diagnostic for transcription/normalization only; it is not a proof of
uniform convergence or of the analytic comparison theorem.
"""
from __future__ import annotations
import json
import math
import random
from pathlib import Path
import mpmath as mp

mp.mp.dps = 320
rng = random.Random(20260830)


def u(x: mp.mpf) -> mp.mpf:
    return 2 * mp.atan(mp.e ** x)


def annulus_ratio(xistar: mp.mpf, rho: mp.mpf, x: mp.mpf) -> mp.mpf:
    um = u(xistar - rho)
    up = u(xistar + rho)
    du = up - um
    ux = u(xistar + x)
    y = mp.pi * (ux - um) / du
    return (mp.pi / du) ** 2 * mp.sin(ux) ** 2 / mp.sin(y) ** 2


def residual_ratio(rho: float, r: float) -> float:
    rrho = math.tanh(rho / 2)
    z = math.tanh(r / 2)
    return rrho**2 * (1 - z**2) ** 2 / (rrho**2 - z**2) ** 2

annulus_min = mp.inf
annulus_max = mp.mpf(0)
for _ in range(25000):
    rho = mp.mpf(rng.uniform(2.5, 18.0))
    r = min(mp.mpf(rng.uniform(0.0, 2.0)), rho / 3)
    xistar = mp.mpf(rng.uniform(-8.0, 8.0)) * rho
    val = annulus_ratio(xistar, rho, r)
    annulus_min = min(annulus_min, val)
    annulus_max = max(annulus_max, val)
    if val < 1 - mp.mpf("1e-40"):
        raise AssertionError((xistar, rho, r, val))

# Convergence on fixed inner windows, including centers escaping into either end.
conv = []
for rho in [4, 6, 8, 10, 12, 16]:
    err = mp.mpf(0)
    for c in [-12, -4, -2, -1, 0, 1, 2, 4, 12]:
        for x in [-1.5, -0.75, 0, 0.75, 1.5]:
            err = max(err, abs(annulus_ratio(mp.mpf(c * rho), mp.mpf(rho), mp.mpf(x)) - 1))
    conv.append([rho, float(err)])

residual_min = float("inf")
residual_max = 0.0
for _ in range(25000):
    rho = rng.uniform(2.0, 15.0)
    r = rng.uniform(0.0, rho - 0.25)
    val = residual_ratio(rho, r)
    residual_min = min(residual_min, val)
    residual_max = max(residual_max, val)
    if val < 1 - 1e-12:
        raise AssertionError((rho, r, val))

result = {
    "status": "PASS",
    "annulus_samples": 25000,
    "annulus_ratio_min": float(annulus_min),
    "annulus_ratio_max": float(annulus_max),
    "annulus_fixed_window_convergence": conv,
    "residual_samples": 25000,
    "residual_ratio_min": residual_min,
    "residual_ratio_max": residual_max,
    "disclaimer": "Numerical transcription audit only; not a proof of the analytic theorem.",
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2), encoding='utf-8')
print("Intrinsic complete-window numerical audit passed.")
print(json.dumps(result, indent=2))
print(f"wrote {out}")
