#!/usr/bin/env python3
"""Finite certificate for the complex cusp-phase orientation local system.

Builds the Desargues incidence graph of 2- and 3-subsets of a 5-set,
computes the ordered-triple sign cochain, verifies that it is a nontrivial
Z/2 cohomology class, and checks that all girth-six cycles have holonomy -1.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path


def permutation_sign(seq: tuple[int, ...]) -> int:
    inv = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
    return -1 if inv % 2 else 1


def rank_gf2(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] & 1), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(m):
            if i != r and (a[i][c] & 1):
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def canonical_cycle(cycle):
    reps = []
    for orient in (list(cycle), list(reversed(cycle))):
        for k in range(len(cycle)):
            reps.append(tuple(orient[k:] + orient[:k]))
    return min(reps, key=repr)


def main() -> None:
    two = list(itertools.combinations(range(5), 2))
    three = list(itertools.combinations(range(5), 3))
    vertices = [("e", e) for e in two] + [("t", t) for t in three]
    vertex_index = {v: i for i, v in enumerate(vertices)}
    incidences = [(e, t) for e in two for t in three if set(e).issubset(t)]

    epsilon = {}
    for e, t in incidences:
        k = next(x for x in t if x not in e)
        epsilon[(e, t)] = permutation_sign((e[0], e[1], k))

    coboundary = [[0] * len(vertices) for _ in incidences]
    phase = [0] * len(incidences)
    for row, (e, t) in enumerate(incidences):
        coboundary[row][vertex_index[("e", e)]] = 1
        coboundary[row][vertex_index[("t", t)]] = 1
        phase[row] = int(epsilon[(e, t)] == -1)

    rank = rank_gf2(coboundary)
    augmented_rank = rank_gf2([row + [phase[i]] for i, row in enumerate(coboundary)])
    if rank != 19 or augmented_rank != 20:
        raise AssertionError((rank, augmented_rank))

    adjacency = {v: [] for v in vertices}
    for e, t in incidences:
        ve, vt = ("e", e), ("t", t)
        adjacency[ve].append(vt)
        adjacency[vt].append(ve)

    cycles = set()
    for start in vertices:
        def dfs(path):
            if len(path) == 6:
                if start in adjacency[path[-1]]:
                    cycles.add(canonical_cycle(path))
                return
            for nxt in adjacency[path[-1]]:
                if nxt == start or nxt in path:
                    continue
                dfs(path + [nxt])
        dfs([start])

    def edge_sign(v, w):
        if v[0] == "e":
            e, t = v[1], w[1]
        else:
            e, t = w[1], v[1]
        return epsilon[(e, t)]

    holonomies = []
    for cycle in sorted(cycles, key=repr):
        hol = 1
        for i in range(6):
            hol *= edge_sign(cycle[i], cycle[(i + 1) % 6])
        holonomies.append(hol)
    if len(cycles) != 20 or set(holonomies) != {-1}:
        raise AssertionError((len(cycles), holonomies))

    explicit = [
        ("e", (0, 1)),
        ("t", (0, 1, 2)),
        ("e", (1, 2)),
        ("t", (1, 2, 3)),
        ("e", (1, 3)),
        ("t", (0, 1, 3)),
    ]
    explicit_holonomy = 1
    for i in range(6):
        explicit_holonomy *= edge_sign(explicit[i], explicit[(i + 1) % 6])
    if explicit_holonomy != -1:
        raise AssertionError(explicit_holonomy)

    # Ordering-independence: pull the sign cochain back by every permutation
    # of the five labels.  The change must be the vertex coboundary given by
    # the induced orientation signs on 2- and 3-subsets.
    checked_permutations = 0
    for sigma_tuple in itertools.permutations(range(5)):
        sigma = {i: sigma_tuple[i] for i in range(5)}
        for e, t in incidences:
            e_image_ordered = (sigma[e[0]], sigma[e[1]])
            e_image = tuple(sorted(e_image_ordered))
            t_image_ordered = tuple(sigma[i] for i in t)
            t_image = tuple(sorted(t_image_ordered))
            b_e = permutation_sign(e_image_ordered)
            c_t = permutation_sign(t_image_ordered)
            pulled = epsilon[(e_image, t_image)]
            expected = c_t * b_e * epsilon[(e, t)]
            if pulled != expected:
                raise AssertionError((sigma_tuple, e, t, pulled, expected))
        checked_permutations += 1

    payload = {
        "vertices": len(vertices),
        "edges": len(incidences),
        "b1": len(incidences) - len(vertices) + 1,
        "coboundary_rank_gf2": rank,
        "augmented_rank_gf2": augmented_rank,
        "phase_class_nontrivial": True,
        "order_of_phase_class": 2,
        "number_of_simple_6_cycles": len(cycles),
        "all_6_cycle_holonomies": -1,
        "explicit_cycle_holonomy": explicit_holonomy,
        "label_permutations_checked": checked_permutations,
        "ordering_change_is_vertex_coboundary": True,
        "incidence_sign_counts": {
            "+1": sum(v == 1 for v in epsilon.values()),
            "-1": sum(v == -1 for v in epsilon.values()),
        },
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Complex phase orientation certificate passed.")
    print(out.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
