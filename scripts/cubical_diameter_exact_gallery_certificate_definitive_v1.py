#!/usr/bin/env python3
"""Exact gallery certificate for diam(C_5)=sqrt(13).

The square complex is
    C_5 = union Q_{i;jk},
    Q_{i;jk} = e_i + [0,1] e_j + [0,1] e_k,
for distinct i,j,k in {0,...,4}.  The script uses only exact integer
arithmetic to:

1. enumerate the 30 squares and the nine S_5-orbits of unordered pairs;
2. verify every gallery used in the analytic diameter proof;
3. unfold each gallery into the Euclidean plane and verify the endpoint
   affine maps quoted in the manuscript;
4. record the elementary quadratic bounds proving diam(C_5)<=sqrt(13).

The lower bound and equality classification use the piecewise-linear
calibration and the ridge-shortening argument written in the manuscript.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path
from typing import Dict, List, Sequence, Tuple, FrozenSet

Vec = Tuple[int, int]
Mat = Tuple[Tuple[int, int], Tuple[int, int]]
Affine = Tuple[Mat, Vec]
Cell = Tuple[int, int, int]
Label = FrozenSet[int]


def add(x: Vec, y: Vec) -> Vec:
    return (x[0] + y[0], x[1] + y[1])


def sub(x: Vec, y: Vec) -> Vec:
    return (x[0] - y[0], x[1] - y[1])


def mat_vec(m: Mat, x: Vec) -> Vec:
    return (
        m[0][0] * x[0] + m[0][1] * x[1],
        m[1][0] * x[0] + m[1][1] * x[1],
    )


def cross(x: Vec, y: Vec) -> int:
    return x[0] * y[1] - x[1] * y[0]


ORTHOGONAL_SIGNED_PERMUTATIONS: Tuple[Mat, ...] = (
    ((1, 0), (0, 1)),
    ((1, 0), (0, -1)),
    ((-1, 0), (0, 1)),
    ((-1, 0), (0, -1)),
    ((0, 1), (1, 0)),
    ((0, 1), (-1, 0)),
    ((0, -1), (1, 0)),
    ((0, -1), (-1, 0)),
)


def cells() -> List[Cell]:
    ans: List[Cell] = []
    for triple in itertools.combinations(range(5), 3):
        for distinguished in triple:
            j, k = sorted(set(triple) - {distinguished})
            ans.append((distinguished, j, k))
    return ans


CELLS = cells()
CELL_INDEX = {cell: i for i, cell in enumerate(CELLS)}


def cell_vertices(cell: Cell) -> Dict[Vec, Label]:
    i, j, k = cell
    return {
        (0, 0): frozenset({i}),
        (1, 0): frozenset({i, j}),
        (0, 1): frozenset({i, k}),
        (1, 1): frozenset({i, j, k}),
    }


CELL_VERTICES = [cell_vertices(cell) for cell in CELLS]


def local_coordinate(cell_index: int, label: Label) -> Vec:
    for coordinate, vertex_label in CELL_VERTICES[cell_index].items():
        if vertex_label == label:
            return coordinate
    raise KeyError((cell_index, label))


def shared_edge(a: int, b: int) -> Tuple[Label, Label]:
    common = set(CELL_VERTICES[a].values()) & set(CELL_VERTICES[b].values())
    if len(common) != 2:
        raise AssertionError(f"cells {a},{b} do not share a full edge")
    labels = tuple(sorted(common, key=lambda s: (len(s), tuple(sorted(s)))))
    ca = [local_coordinate(a, label) for label in labels]
    cb = [local_coordinate(b, label) for label in labels]
    if sum(abs(ca[0][i] - ca[1][i]) for i in range(2)) != 1:
        raise AssertionError("common vertices are not an edge in first square")
    if sum(abs(cb[0][i] - cb[1][i]) for i in range(2)) != 1:
        raise AssertionError("common vertices are not an edge in second square")
    return labels  # type: ignore[return-value]


def unfold_next(current: Affine, a: int, b: int) -> Affine:
    matrix_a, shift_a = current
    label1, label2 = shared_edge(a, b)
    pa1, pa2 = local_coordinate(a, label1), local_coordinate(a, label2)
    pb1, pb2 = local_coordinate(b, label1), local_coordinate(b, label2)
    p1 = add(mat_vec(matrix_a, pa1), shift_a)
    p2 = add(mat_vec(matrix_a, pa2), shift_a)
    edge = sub(p2, p1)

    # Twice the centroid is integral, so use doubled vectors for side tests.
    centroid_a_twice = add(
        mat_vec(matrix_a, (1, 1)), (2 * shift_a[0], 2 * shift_a[1])
    )
    side_a = cross(edge, sub(centroid_a_twice, (2 * p1[0], 2 * p1[1])))

    candidates: List[Affine] = []
    for matrix_b in ORTHOGONAL_SIGNED_PERMUTATIONS:
        if mat_vec(matrix_b, sub(pb2, pb1)) != edge:
            continue
        shift_b = sub(p1, mat_vec(matrix_b, pb1))
        centroid_b_twice = add(
            mat_vec(matrix_b, (1, 1)), (2 * shift_b[0], 2 * shift_b[1])
        )
        side_b = cross(edge, sub(centroid_b_twice, (2 * p1[0], 2 * p1[1])))
        if side_a * side_b < 0:
            candidates.append((matrix_b, shift_b))
    if len(candidates) != 1:
        raise AssertionError(f"unfolding ambiguity for {a}->{b}: {candidates}")
    return candidates[0]


def unfold_gallery(gallery_data: Sequence[int]) -> List[Affine]:
    if not gallery_data:
        raise ValueError("gallery cannot be empty")
    embeddings: List[Affine] = [(((1, 0), (0, 1)), (0, 0))]
    for a, b in zip(gallery_data, gallery_data[1:]):
        embeddings.append(unfold_next(embeddings[-1], a, b))
    return embeddings


def embedding_bounds(embedding: Affine) -> Tuple[int, int, int, int]:
    matrix, shift = embedding
    points = [
        add(mat_vec(matrix, p), shift)
        for p in ((0, 0), (1, 0), (0, 1), (1, 1))
    ]
    return (
        min(p[0] for p in points),
        max(p[0] for p in points),
        min(p[1] for p in points),
        max(p[1] for p in points),
    )


def gallery_word(embeddings: Sequence[Affine]) -> str:
    lower_left = [(embedding_bounds(e)[0], embedding_bounds(e)[2]) for e in embeddings]
    letters: List[str] = []
    for p, q in zip(lower_left, lower_left[1:]):
        delta = sub(q, p)
        table = {(1, 0): "R", (-1, 0): "L", (0, 1): "U", (0, -1): "D"}
        if delta not in table:
            raise AssertionError(f"non-unit gallery step {delta}")
        letters.append(table[delta])
    return "".join(letters)


def idx(cell: Cell) -> int:
    return CELL_INDEX[cell]


def gallery(*cell_data: Cell) -> Tuple[int, ...]:
    return tuple(idx(cell) for cell in cell_data)


def act_cell(cell_index: int, permutation: Sequence[int]) -> int:
    i, j, k = CELLS[cell_index]
    jj, kk = sorted((permutation[j], permutation[k]))
    return CELL_INDEX[(permutation[i], jj, kk)]


def canonical_pair(a: int, b: int) -> Tuple[int, int]:
    images = []
    for permutation in itertools.permutations(range(5)):
        aa, bb = act_cell(a, permutation), act_cell(b, permutation)
        images.append(tuple(sorted((aa, bb))))
    return min(images)


def orbit_data() -> List[Tuple[Tuple[int, int], int]]:
    buckets: Dict[Tuple[int, int], int] = {}
    for a in range(30):
        for b in range(a, 30):
            key = canonical_pair(a, b)
            buckets[key] = buckets.get(key, 0) + 1
    result = sorted(buckets.items())
    assert len(result) == 9
    assert sum(size for _, size in result) == 465
    return result


Q = lambda i, j, k: (i, min(j, k), max(j, k))

GALLERIES: Dict[str, List[Tuple[int, ...]]] = {
    "orbit5_vertical_strip": [
        gallery(Q(0, 1, 2), Q(0, 1, 3), Q(3, 0, 1)),
    ],
    "orbit8_right_left_strips": [
        gallery(Q(0, 1, 2), Q(1, 0, 2), Q(1, 2, 3), Q(3, 1, 2)),
        gallery(Q(0, 1, 2), Q(0, 2, 3), Q(3, 0, 2), Q(3, 1, 2)),
    ],
    "orbit7_LDD_DLD_DDL": [
        gallery(Q(0, 1, 2), Q(0, 2, 4), Q(0, 3, 4), Q(3, 0, 4)),
        gallery(Q(0, 1, 2), Q(0, 1, 3), Q(0, 3, 4), Q(3, 0, 4)),
        gallery(Q(0, 1, 2), Q(0, 1, 3), Q(3, 0, 1), Q(3, 0, 4)),
    ],
    "orbit9_right_shuffles": [
        gallery(Q(0, 1, 2), Q(1, 0, 2), Q(1, 2, 3), Q(3, 1, 2), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(1, 0, 2), Q(1, 2, 3), Q(1, 3, 4), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(1, 0, 2), Q(1, 0, 4), Q(1, 3, 4), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(0, 1, 4), Q(1, 0, 4), Q(1, 3, 4), Q(3, 1, 4)),
    ],
    "orbit9_left_shuffles": [
        gallery(Q(0, 1, 2), Q(0, 2, 3), Q(3, 0, 2), Q(3, 1, 2), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(0, 2, 3), Q(3, 0, 2), Q(3, 0, 4), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(0, 2, 3), Q(0, 3, 4), Q(3, 0, 4), Q(3, 1, 4)),
        gallery(Q(0, 1, 2), Q(0, 1, 4), Q(0, 3, 4), Q(3, 0, 4), Q(3, 1, 4)),
    ],
    "orbit9_ridge_shortening": [
        gallery(Q(0, 1, 2), Q(1, 0, 2), Q(1, 0, 3), Q(1, 3, 4), Q(3, 1, 4)),
    ],
}

EXPECTED_ENDPOINT_AFFINE: Dict[str, Affine] = {
    "orbit5_vertical_strip": (((0, 1), (1, 0)), (0, -2)),
    "orbit8_right": (((-1, 0), (0, 1)), (4, 0)),
    "orbit8_left": (((-1, 0), (0, 1)), (-2, 0)),
    "orbit7": (((0, -1), (1, 0)), (0, -2)),
    "orbit9_right": (((-1, 0), (0, -1)), (4, 0)),
    "orbit9_left": (((-1, 0), (0, -1)), (-2, 0)),
    "orbit9_ridge": (((0, 1), (1, 0)), (2, -2)),
}


def verify_group(name: str, expected: Affine) -> List[dict[str, object]]:
    records: List[dict[str, object]] = []
    for g in GALLERIES[name]:
        embeddings = unfold_gallery(g)
        endpoint = embeddings[-1]
        if endpoint != expected:
            raise AssertionError(f"{name}: endpoint {endpoint}, expected {expected}")
        records.append(
            {
                "indices": list(g),
                "cells": [list(CELLS[i]) for i in g],
                "word": gallery_word(embeddings),
                "square_bounds": [list(embedding_bounds(e)) for e in embeddings],
                "endpoint_matrix": [list(row) for row in endpoint[0]],
                "endpoint_shift": list(endpoint[1]),
            }
        )
    return records


def main() -> None:
    orbit_info = orbit_data()
    assert [size for _, size in orbit_info] == [30, 30, 60, 60, 120, 15, 60, 30, 60]

    records: Dict[str, object] = {
        "number_of_squares": len(CELLS),
        "number_of_unordered_square_pairs": 465,
        "number_of_S5_orbits": len(orbit_info),
        "orbit_sizes": [size for _, size in orbit_info],
    }

    records["orbit5_vertical_strip"] = verify_group(
        "orbit5_vertical_strip", EXPECTED_ENDPOINT_AFFINE["orbit5_vertical_strip"]
    )

    orbit8_records = []
    for g, key in zip(
        GALLERIES["orbit8_right_left_strips"], ("orbit8_right", "orbit8_left")
    ):
        endpoint = unfold_gallery(g)[-1]
        assert endpoint == EXPECTED_ENDPOINT_AFFINE[key]
        embeddings = unfold_gallery(g)
        orbit8_records.append(
            {
                "key": key,
                "indices": list(g),
                "cells": [list(CELLS[i]) for i in g],
                "word": gallery_word(embeddings),
                "square_bounds": [list(embedding_bounds(e)) for e in embeddings],
                "endpoint_matrix": [list(row) for row in endpoint[0]],
                "endpoint_shift": list(endpoint[1]),
            }
        )
    records["orbit8_strips"] = orbit8_records

    records["orbit7_shuffles"] = verify_group(
        "orbit7_LDD_DLD_DDL", EXPECTED_ENDPOINT_AFFINE["orbit7"]
    )
    records["orbit9_right_shuffles"] = verify_group(
        "orbit9_right_shuffles", EXPECTED_ENDPOINT_AFFINE["orbit9_right"]
    )
    records["orbit9_left_shuffles"] = verify_group(
        "orbit9_left_shuffles", EXPECTED_ENDPOINT_AFFINE["orbit9_left"]
    )
    records["orbit9_ridge_shortening"] = verify_group(
        "orbit9_ridge_shortening", EXPECTED_ENDPOINT_AFFINE["orbit9_ridge"]
    )

    expected_words = {
        "orbit5_vertical_strip": ["DD"],
        "orbit8_strips": ["RRR", "LLL"],
        "orbit7_shuffles": ["LDD", "DLD", "DDL"],
        "orbit9_right_shuffles": ["RRRD", "RRDR", "RDRR", "DRRR"],
        "orbit9_left_shuffles": ["LLLD", "LLDL", "LDLL", "DLLL"],
        "orbit9_ridge_shortening": ["RDRD"],
    }
    for key, expected in expected_words.items():
        actual = [record["word"] for record in records[key]]  # type: ignore[index]
        if actual != expected:
            raise AssertionError(f"{key}: words {actual}, expected {expected}")
    records["expected_words"] = expected_words

    records["exact_bounds"] = {
        "orbit5": "(a-d)^2+(b-c+2)^2 <= 1+9 = 10",
        "orbit8": "min((s+2)^2,(4-s)^2)+(b-d)^2 <= 9+1 = 10, 0<=s<=2",
        "orbit7": "(a+d)^2+(b-c+2)^2 <= 4+9 = 13",
        "orbit9": "min((s+2)^2,(4-s)^2)+u^2 <= 9+4 = 13, 0<=s,u<=2",
        "orbit9_ridge": "13-2a+2a^2 = 13-2a(1-a) < 13 for 0<a<1",
    }

    print("Exact gallery certificate passed.")
    print(
        f"30 squares; 465 unordered pairs; orbit sizes {records['orbit_sizes']}"
    )
    print("All listed galleries unfold with the integer affine maps used in the manuscript.")
    print(
        "Analytic conclusion: diam(C_5)=sqrt(13); equality only at complementary size-2/size-3 vertices."
    )

    out_path = Path(__file__).with_suffix(".json")
    out_path.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
