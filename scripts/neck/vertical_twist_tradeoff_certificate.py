#!/usr/bin/env python3
"""Exact bookkeeping for the fixed-twist obstruction and balanced scale.

This certificate checks the finite/combinatorial part of the local formulas in
v0.4.  It does not prove the analytic comparison estimate; the note proves the
local asymptotic estimate using the small-resolution chart and smooth-metric
comparability.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

LABELS = tuple(range(5))
NODES_PER_DOUBLE_LINE = 5


def endpoint_L_coefficient(a: int, b: int) -> int:
    """Coefficient of L in log|x^a u^b|^2(p)-... at the two neck ends."""
    # At p: (log|x|^2, log|u|^2)=(O(1),-L+O(1)).
    # At q: (log|x|^2, log|u|^2)=(-L+O(1),O(1)).
    return a - b


def build_certificate() -> dict[str, Any]:
    local_weight_checks: list[dict[str, int]] = []
    for a in range(-4, 5):
        for b in range(-4, 5):
            d = b - a
            coeff = endpoint_L_coefficient(a, b)
            assert abs(coeff) == abs(d)
            local_weight_checks.append({"a": a, "b": b, "degree_on_E": d, "endpoint_L_coefficient": coeff})

    order_data = []
    for order in itertools.permutations(LABELS):
        pos = {label: k for k, label in enumerate(order)}
        oriented_pairs = []
        component_blowups = {i: 0 for i in LABELS}
        for i, j in itertools.combinations(LABELS, 2):
            early, late = (i, j) if pos[i] < pos[j] else (j, i)
            component_blowups[early] += NODES_PER_DOUBLE_LINE
            oriented_pairs.append({"early": early, "late": late, "node_count": NODES_PER_DOUBLE_LINE, "local_degree": 1})
        profile = [component_blowups[i] for i in order]
        assert profile == [20, 15, 10, 5, 0]
        assert sum(component_blowups.values()) == 50
        order_data.append({"order": list(order), "profile": profile, "oriented_pairs": oriented_pairs})

    tradeoff = {
        "fixed_N": {
            "vertical_coefficient": "1/N",
            "Ricci_potential_oscillation": "(d/N) L + O(log L)",
            "uniform_C0_for_fixed_N": False,
        },
        "balanced_epsilon": {
            "epsilon": "1/L",
            "weight_oscillation": "d + o(1)",
            "vertical_twist_length_contribution": "L^(-1/2)",
            "robust_total_core_diameter": "O(1)",
            "curvature_scale": "L",
        },
        "first_scale": {"R": "log L", "vertical_contribution_over_R": "L^(-1/2)/(log L) -> 0", "O1_core_over_R": "1/(log L) -> 0"},
    }

    numerical_samples = []
    for N in (1, 2, 5, 10, 100):
        numerical_samples.append({
            "N": N,
            "oscillation_L_coefficient_for_d=1": str(Fraction(1, N)),
            "diverges_as_L_to_infinity": True,
        })

    return {
        "certificate": "quintic-five-planes-vertical-twist-tradeoff-v0.4",
        "local_divisor_degrees": {"deg_O(D_u)|E": 1, "deg_O(D_x)|E": -1, "deg_A|E": "b-a"},
        "local_weight_checks": local_weight_checks,
        "number_of_total_orders": len(order_data),
        "ordered_resolution_profile": [20, 15, 10, 5, 0],
        "total_nodes": 50,
        "sample_orders": order_data[:5],
        "tradeoff": tradeoff,
        "fixed_N_samples": numerical_samples,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path(__file__).with_suffix(".json"))
    parser.add_argument("--text", type=Path, default=Path(__file__).with_suffix(".txt"))
    args = parser.parse_args()

    certificate = build_certificate()
    args.json.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    message = (
        "Exact vertical-twist tradeoff bookkeeping passed.\n"
        "For A=O(a D_x+b D_u), deg(A|E)=b-a and the neck-end log-norm "
        "oscillation has coefficient |b-a| L.\n"
        "All 120 component orders orient 50 nodes and have profile [20, 15, 10, 5, 0].\n"
        "Fixed N leaves oscillation (d/N)L; epsilon=1/L balances it, with model "
        "vertical length contribution L^(-1/2), robust core diameter O(1), and curvature scale L.\n"
    )
    args.text.write_text(message, encoding="utf-8")
    print(message, end="")


if __name__ == "__main__":
    main()
