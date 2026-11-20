#!/usr/bin/env python3
"""Symbolic certificate for the local node-weight and determinant identities in v0.4."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp


def build_certificate() -> dict[str, Any]:
    a, b, d, L, N = sp.symbols("a b d L N", positive=True)

    H = a**-2 + b**-2
    chi = (a + b)**2 / (a**2 * b**2)
    ratio = sp.factor(sp.simplify(H / chi))
    expected = sp.factor((a**2 + b**2) / (a + b)**2)
    assert sp.simplify(ratio - expected) == 0

    lower_numerator = sp.expand(2 * (a**2 + b**2) - (a + b)**2)
    upper_numerator = sp.expand((a + b)**2 - (a**2 + b**2))
    assert sp.factor(lower_numerator) == (a - b)**2
    assert sp.factor(upper_numerator) == 2 * a * b

    fixed_oscillation = d * L / N
    balanced = sp.simplify(fixed_oscillation.subs(N, L))
    assert balanced == d

    return {
        "certificate": "quintic-five-planes-node-weight-identity-v0.4",
        "poincare_radial_coefficient": str(H),
        "volume_normalization": str(chi),
        "exact_ratio": str(ratio),
        "lower_bound_certificate": "2(a^2+b^2)-(a+b)^2=(a-b)^2 >= 0",
        "upper_bound_certificate": "(a+b)^2-(a^2+b^2)=2ab >= 0",
        "ratio_interval": ["1/2", "1"],
        "fixed_twist_leading_oscillation": str(fixed_oscillation),
        "balanced_effective_coefficient_epsilon_equal_1_over_L": str(balanced),
        "interpretation": {
            "fixed_N": "order L oscillation for nonzero vertical degree d",
            "epsilon_equal_1_over_L": "order-one weight oscillation",
            "warning": "The identities are local; they do not prove global positivity, curvature bounds, or the actual KE comparison theorem.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path(__file__).with_suffix(".json"))
    parser.add_argument("--text", type=Path, default=Path(__file__).with_suffix(".txt"))
    args = parser.parse_args()

    cert = build_certificate()
    args.json.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    message = (
        "Exact node-weight identity certificate passed.\n"
        "(a^{-2}+b^{-2}) / ((a+b)^2/(a^2 b^2)) = (a^2+b^2)/(a+b)^2 in [1/2,1].\n"
        "A fixed vertical coefficient leaves order-L oscillation; coefficient 1/L balances it to order one.\n"
    )
    args.text.write_text(message, encoding="utf-8")
    print(message, end="")


if __name__ == "__main__":
    main()
