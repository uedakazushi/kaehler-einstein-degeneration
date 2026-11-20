#!/usr/bin/env python3
"""Exact finite certificate for the A4 chamber structure of ordered small resolutions.

The certificate concerns the 120 projective models obtained by ordering the five
components and blowing up their component ideals successively.  It does not
classify all globally projective choices among the 2^50 local analytic small
resolutions.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

LABELS = tuple(range(5))
NODES_PER_EDGE = 5


def oriented_edges(order: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    pos = {v: k for k, v in enumerate(order)}
    return frozenset((i, j) if pos[i] < pos[j] else (j, i)
                     for i, j in itertools.combinations(LABELS, 2))


def profile(order: tuple[int, ...]) -> list[int]:
    pos = {v: k for k, v in enumerate(order)}
    counts = {
        i: NODES_PER_EDGE * sum(pos[i] < pos[j] for j in LABELS if j != i)
        for i in LABELS
    }
    return [counts[i] for i in order]


def chamber_weights(order: tuple[int, ...]) -> dict[int, int]:
    # Strictly increasing integral weights in the chamber, modulo common shift.
    return {label: rank for rank, label in enumerate(order)}


def build_certificate() -> dict[str, Any]:
    orders = list(itertools.permutations(LABELS))
    orientations = {oriented_edges(order) for order in orders}
    assert len(orders) == 120
    assert len(orientations) == 120

    chamber_rows: list[dict[str, Any]] = []
    for order in orders:
        edges = oriented_edges(order)
        weights = chamber_weights(order)
        degrees = []
        for early, late in sorted(edges):
            degree = weights[late] - weights[early]
            assert degree > 0
            degrees.append({
                "double_line": [early, late],
                "exceptional_curves": NODES_PER_EDGE,
                "degree_Dlambda_on_each_curve": degree,
            })
        assert profile(order) == [20, 15, 10, 5, 0]
        chamber_rows.append({
            "order": list(order),
            "weights": {str(k): v for k, v in weights.items()},
            "profile_in_order_coordinates": profile(order),
            "positive_degrees": degrees,
        })

    adjacency: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    adjacent_rows: list[dict[str, Any]] = []
    for order in orders:
        for r in range(4):
            swapped = list(order)
            i, j = swapped[r], swapped[r + 1]
            swapped[r], swapped[r + 1] = swapped[r + 1], swapped[r]
            other = tuple(swapped)
            edge = tuple(sorted((order, other)))
            if edge in adjacency:
                continue
            adjacency.add(edge)
            changed = oriented_edges(order) ^ oriented_edges(other)
            # Symmetric difference contains the two opposite oriented versions.
            assert changed == frozenset({(i, j), (j, i)})
            adjacent_rows.append({
                "orders": [list(order), list(other)],
                "swapped_labels": [i, j],
                "flopped_double_line": sorted([i, j]),
                "simultaneously_flopped_curves": NODES_PER_EDGE,
            })

    # 1-skeleton of the 4-dimensional permutohedron: 120*4/2 = 240 edges.
    assert len(adjacency) == 240

    return {
        "certificate": "quintic-five-planes-ordered-A4-chambers-v0.4",
        "number_of_labels": 5,
        "number_of_double_lines": 10,
        "nodes_per_double_line": NODES_PER_EDGE,
        "total_exceptional_curves": 50,
        "number_of_ordered_chambers": len(orders),
        "number_of_transitive_tournaments": len(orientations),
        "braid_arrangement": "A4: lambda_i=lambda_j modulo common translation",
        "component_degree_formula": "D_lambda . E_(ij,p) = lambda_j-lambda_i for i earlier than j",
        "ordered_profile": [20, 15, 10, 5, 0],
        "permutohedron_adjacency_edges": len(adjacency),
        "adjacent_swap_flop_count": NODES_PER_EDGE,
        "sample_chambers": chamber_rows[:8],
        "sample_adjacent_flops": adjacent_rows[:12],
        "scope_warning": "This certifies the 120 ordered projective models, not a classification of all projective globalizations of the 2^50 local analytic choices.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path(__file__).with_suffix(".json"))
    parser.add_argument("--text", type=Path, default=Path(__file__).with_suffix(".txt"))
    args = parser.parse_args()

    cert = build_certificate()
    args.json.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    message = (
        "Exact A4 ordered-chamber certificate passed.\n"
        "120 total orders give 120 transitive orientations of K5.\n"
        "For an oriented edge i<j, D_lambda.E=lambda_j-lambda_i>0.\n"
        "The chamber adjacency graph has 240 edges; each adjacent swap flops the five curves over one double line.\n"
    )
    args.text.write_text(message, encoding="utf-8")
    print(message, end="")


if __name__ == "__main__":
    main()
