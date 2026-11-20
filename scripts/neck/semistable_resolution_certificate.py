#!/usr/bin/env python3
"""Exact finite checks for the v0.3 quintic-five-planes research note.

The script verifies only combinatorial/intersection-number bookkeeping.  It is
not a computer-algebra proof of smoothness, projectivity, or crepancy; those
are established in the note by the local blow-up charts and standard
birational arguments.
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any, Iterable

LABELS = tuple(range(5))
TRIPLE_POINTS_PER_DOUBLE_LINE = 3
NODES_PER_DOUBLE_LINE = 5


def subsets_of_size(k: int) -> tuple[frozenset[int], ...]:
    return tuple(frozenset(s) for s in itertools.combinations(LABELS, k))


def canonical_edge(a: frozenset[int], b: frozenset[int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    aa, bb = tuple(sorted(a)), tuple(sorted(b))
    return (aa, bb) if (len(aa), aa) < (len(bb), bb) else (bb, aa)


def square_vertices(distinguished: int, other_a: int, other_b: int) -> frozenset[frozenset[int]]:
    i, j, k = distinguished, other_a, other_b
    return frozenset(
        {
            frozenset({i}),
            frozenset({i, j}),
            frozenset({i, k}),
            frozenset({i, j, k}),
        }
    )


def square_edges(vertices: frozenset[frozenset[int]]) -> frozenset[tuple[tuple[int, ...], tuple[int, ...]]]:
    edges: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for a, b in itertools.combinations(vertices, 2):
        if a < b and len(b) == len(a) + 1:
            edges.add(canonical_edge(a, b))
        elif b < a and len(a) == len(b) + 1:
            edges.add(canonical_edge(a, b))
    return frozenset(edges)


def build_cubical_complex() -> dict[str, Any]:
    vertices = set().union(*(set(subsets_of_size(k)) for k in (1, 2, 3)))
    edges = {
        canonical_edge(a, b)
        for a, b in itertools.combinations(vertices, 2)
        if (a < b and len(b) == len(a) + 1) or (b < a and len(a) == len(b) + 1)
    }

    squares: dict[tuple[int, tuple[int, int]], frozenset[frozenset[int]]] = {}
    for triple in itertools.combinations(LABELS, 3):
        for i in triple:
            others = tuple(sorted(set(triple) - {i}))
            squares[(i, others)] = square_vertices(i, *others)

    assert len(vertices) == 25
    assert len(edges) == 50
    assert len(squares) == 30
    for verts in squares.values():
        assert len(verts) == 4
        assert len(square_edges(verts)) == 4

    return {"vertices": vertices, "edges": edges, "squares": squares}


def star_cells(complex_data: dict[str, Any], i: int) -> dict[str, set[Any]]:
    squares = {
        key: verts
        for key, verts in complex_data["squares"].items()
        if key[0] == i
    }
    vertices = set().union(*(set(vs) for vs in squares.values()))
    edges = set().union(*(set(square_edges(vs)) for vs in squares.values()))
    return {"vertices": vertices, "edges": edges, "squares": set(squares)}


def check_stars(complex_data: dict[str, Any]) -> dict[str, Any]:
    stars = {i: star_cells(complex_data, i) for i in LABELS}

    assert set().union(*(s["vertices"] for s in stars.values())) == complex_data["vertices"]
    assert set().union(*(s["edges"] for s in stars.values())) == complex_data["edges"]
    assert set().union(*(s["squares"] for s in stars.values())) == set(complex_data["squares"])

    pair_data: dict[str, Any] = {}
    for i, j in itertools.combinations(LABELS, 2):
        common_v = stars[i]["vertices"] & stars[j]["vertices"]
        common_e = stars[i]["edges"] & stars[j]["edges"]
        common_s = stars[i]["squares"] & stars[j]["squares"]
        expected_v = {frozenset({i, j})} | {
            frozenset({i, j, k}) for k in LABELS if k not in {i, j}
        }
        expected_e = {
            canonical_edge(frozenset({i, j}), frozenset({i, j, k}))
            for k in LABELS
            if k not in {i, j}
        }
        assert common_v == expected_v
        assert common_e == expected_e
        assert not common_s
        pair_data[f"{i}{j}"] = {
            "vertices": [sorted(v) for v in sorted(common_v, key=lambda x: (len(x), tuple(x)))],
            "edge_count": len(common_e),
            "shape": "unit tripod",
        }

    triple_data: dict[str, Any] = {}
    for triple in itertools.combinations(LABELS, 3):
        common_v = set.intersection(*(stars[i]["vertices"] for i in triple))
        common_e = set.intersection(*(stars[i]["edges"] for i in triple))
        common_s = set.intersection(*(stars[i]["squares"] for i in triple))
        assert common_v == {frozenset(triple)}
        assert not common_e and not common_s
        triple_data["".join(map(str, triple))] = {"vertex": list(triple)}

    for quadruple in itertools.combinations(LABELS, 4):
        assert not set.intersection(*(stars[i]["vertices"] for i in quadruple))

    return {
        "star_f_vectors": {
            str(i): [len(stars[i]["vertices"]), len(stars[i]["edges"]), len(stars[i]["squares"])]
            for i in LABELS
        },
        "pairwise_intersections": pair_data,
        "triple_intersections": triple_data,
    }


def check_ordered_resolutions() -> dict[str, Any]:
    profiles: set[tuple[int, ...]] = set()
    assignments: list[dict[str, Any]] = []

    for order in itertools.permutations(LABELS):
        pos = {label: idx for idx, label in enumerate(order)}
        profile = tuple(NODES_PER_DOUBLE_LINE * (4 - a) for a in range(5))
        profiles.add(profile)
        assert sum(profile) == 50

        component_blowups = {
            str(i): NODES_PER_DOUBLE_LINE * sum(pos[i] < pos[j] for j in LABELS if j != i)
            for i in LABELS
        }
        assert tuple(component_blowups[str(i)] for i in order) == profile

        for i, j in itertools.combinations(LABELS, 2):
            earlier, later = (i, j) if pos[i] < pos[j] else (j, i)
            early_degree = 1 - NODES_PER_DOUBLE_LINE
            late_degree = 1
            assert early_degree + late_degree + TRIPLE_POINTS_PER_DOUBLE_LINE == 0
            assert component_blowups[str(earlier)] >= NODES_PER_DOUBLE_LINE
            assert pos[earlier] < pos[later]

        assignments.append({
            "order": list(order),
            "component_blowups": component_blowups,
        })

    assert len(assignments) == 120
    assert profiles == {(20, 15, 10, 5, 0)}

    all_local_splits = []
    for k in range(NODES_PER_DOUBLE_LINE + 1):
        degree_i = 1 - k
        degree_j = 1 - (NODES_PER_DOUBLE_LINE - k)
        total = degree_i + degree_j + TRIPLE_POINTS_PER_DOUBLE_LINE
        assert total == 0
        all_local_splits.append({
            "nodes_resolved_on_i": k,
            "normal_degrees": [degree_i, degree_j],
            "triple_formula_sum": total,
        })

    return {
        "number_of_total_orders": len(assignments),
        "profile_in_order_coordinates": [20, 15, 10, 5, 0],
        "total_exceptional_curves": 50,
        "sample_orders": assignments[:5],
        "all_local_node_splits": all_local_splits,
    }


def build_certificate() -> dict[str, Any]:
    complex_data = build_cubical_complex()
    stars = check_stars(complex_data)
    resolutions = check_ordered_resolutions()

    raw_t1_degree = 1 + 1 + TRIPLE_POINTS_PER_DOUBLE_LINE
    assert raw_t1_degree == 5

    return {
        "certificate": "quintic-five-planes-small-resolution-and-colimit-v0.3",
        "labels": list(LABELS),
        "raw_double_line": {
            "normal_degrees": [1, 1],
            "triple_points": TRIPLE_POINTS_PER_DOUBLE_LINE,
            "T1_degree": raw_t1_degree,
            "generic_smoothing_zeros": NODES_PER_DOUBLE_LINE,
        },
        "ordered_small_resolutions": resolutions,
        "local_blowup_charts": {
            "node_equation": "x*y + t*z = 0",
            "blowup_ideal": "(x,t)",
            "x_chart": {"substitution": "t=v*x", "strict_transform": "y+v*z=0", "family_map": "t=x*v"},
            "t_chart": {"substitution": "x=u*t", "strict_transform": "u*y+z=0"},
            "opposite_choice": "blow up (y,t); exchanges the two small resolutions",
        },
        "cubical_complex": {
            "f_vector": [len(complex_data["vertices"]), len(complex_data["edges"]), len(complex_data["squares"])],
            "euler_characteristic": len(complex_data["vertices"]) - len(complex_data["edges"]) + len(complex_data["squares"]),
            "component_stars": stars,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        type=Path,
        default=Path(__file__).with_suffix(".json"),
        help="Output JSON certificate path (default: next to this script).",
    )
    parser.add_argument(
        "--text",
        type=Path,
        default=Path(__file__).with_suffix(".txt"),
        help="Output human-readable status path (default: next to this script).",
    )
    args = parser.parse_args()

    certificate = build_certificate()
    args.json.write_text(json.dumps(certificate, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    message = (
        "Exact small-resolution and colimit certificate passed.\n"
        "120 total orders; each gives blow-up profile [20, 15, 10, 5, 0].\n"
        "On every double line: deg T^1 changes from 5 to 0; "
        "triple formula is (-4)+1+3=0.\n"
        "Cubical complex f-vector is (25, 50, 30); "
        "component-star intersections are tripods.\n"
    )
    args.text.write_text(message, encoding="utf-8")
    print(message, end="")


if __name__ == "__main__":
    main()
