#!/usr/bin/env python3
"""Exact finite-dimensional certificate for untwisted/twisted defect cohomology.

The Desargues incidence graph has ordinary H^1 dimension 11.  The canonical
orientation local system is nontrivial, hence H^0 vanishes and twisted H^1 has
dimension 10.  The script verifies this by exact rational matrix ranks.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


def permutation_sign(seq: tuple[int, ...]) -> int:
    inv = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
    return -1 if inv % 2 else 1


two = list(itertools.combinations(range(5), 2))
three = list(itertools.combinations(range(5), 3))
vertices = [("e", e) for e in two] + [("t", t) for t in three]
vertex_index = {v: i for i, v in enumerate(vertices)}
incidences = [(e, t) for e in two for t in three if set(e).issubset(t)]

ordinary = sp.zeros(len(incidences), len(vertices))
twisted = sp.zeros(len(incidences), len(vertices))

for row, (e, t) in enumerate(incidences):
    k = next(x for x in t if x not in e)
    eps = permutation_sign((e[0], e[1], k))
    ordinary[row, vertex_index[("e", e)]] = -1
    ordinary[row, vertex_index[("t", t)]] = 1
    twisted[row, vertex_index[("e", e)]] = -eps
    twisted[row, vertex_index[("t", t)]] = 1

rank_ordinary = ordinary.rank()
rank_twisted = twisted.rank()
assert rank_ordinary == 19
assert rank_twisted == 20

h0_ordinary = len(vertices) - rank_ordinary
h1_ordinary = len(incidences) - rank_ordinary
h0_twisted = len(vertices) - rank_twisted
h1_twisted = len(incidences) - rank_twisted
assert (h0_ordinary, h1_ordinary) == (1, 11)
assert (h0_twisted, h1_twisted) == (0, 10)

payload = {
    "vertices": len(vertices),
    "incidences": len(incidences),
    "ordinary_coboundary_rank": rank_ordinary,
    "ordinary_H0_dimension": h0_ordinary,
    "ordinary_H1_dimension": h1_ordinary,
    "twisted_coboundary_rank": rank_twisted,
    "twisted_H0_dimension": h0_twisted,
    "twisted_H1_dimension": h1_twisted,
    "interpretation": {
        "even_longitudinal_sector": "ordinary coefficients",
        "odd_longitudinal_sector": "orientation-local-system coefficients",
    },
}

out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print("Defect cohomology certificate passed.")
print(out.read_text(encoding="utf-8"), end="")
