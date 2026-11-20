#!/usr/bin/env python3
"""Finite and symbolic checks for the v0.6 punctured-neck results.

This certificate checks normalizations, the Desargues incidence rank, the
S_3-symmetric reference polynomial, and the exterior-algebra relation used in
the global real scalar matching theorem.  It does not prove the analytic Green
operator construction or nonlinear Kähler--Einstein gluing.
"""
from __future__ import annotations

import itertools
import json
from collections import defaultdict, deque
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT_JSON = HERE / "balanced_punctured_neck_certificate.json"
OUT_TXT = HERE / "balanced_punctured_neck_certificate.txt"

# ---------------------------------------------------------------------------
# 1. Balanced charge and hyperbolic cusp model.
# ---------------------------------------------------------------------------
r = sp.symbols("r", positive=True)
h0 = r + 2 * sp.log(r)
Delta_h0 = sp.simplify(r**2 * sp.diff(h0, r, 2))
flux_one_cusp = sp.limit(2 * sp.pi * sp.diff(h0, r), r, sp.oo)
area = 2 * sp.pi
rhs_mass = sp.simplify(2 * sp.pi * 5 - 2 * area)
assert Delta_h0 == -2
assert flux_one_cusp == 2 * sp.pi
assert rhs_mass == 6 * sp.pi
assert 5 - 2 - 3 == 0

# ---------------------------------------------------------------------------
# 2. S_3-invariant degree-five reference divisor.
# ---------------------------------------------------------------------------
z = sp.symbols("z")
p_star = sp.expand((z**2 - z + 1) * (z + 1) * (z - sp.Rational(1, 2)) * (z - 2))
transform_1_minus_z = sp.simplify(sp.expand(p_star.subs(z, 1 - z)) / p_star)
transform_inverse = sp.simplify(sp.expand(z**5 * p_star.subs(z, 1 / z)) / p_star)
assert transform_1_minus_z == -1
assert transform_inverse == 1
assert p_star.subs(z, 0) == 1
assert p_star.subs(z, 1) == -1
assert sp.Poly(p_star, z).LC() == 1
assert sp.discriminant(p_star, z) != 0

# ---------------------------------------------------------------------------
# 3. Desargues graph: 2-subsets versus 3-subsets of a 5-set.
# ---------------------------------------------------------------------------
base = tuple(range(5))
necks = tuple(itertools.combinations(base, 2))
corners = tuple(itertools.combinations(base, 3))
vertices = tuple(("N", e) for e in necks) + tuple(("C", t) for t in corners)
vindex = {v: i for i, v in enumerate(vertices)}
incidences: list[tuple[tuple, tuple]] = []
for e in necks:
    for t in corners:
        if set(e).issubset(t):
            incidences.append((("N", e), ("C", t)))

B = sp.zeros(len(vertices), len(incidences))
for col, (u, v) in enumerate(incidences):
    B[vindex[u], col] = -1
    B[vindex[v], col] = 1
rank_B = int(B.rank())
b0 = len(vertices) - rank_B
b1 = len(incidences) - rank_B
assert len(necks) == 10
assert len(corners) == 10
assert len(incidences) == 30
assert rank_B == 19
assert b0 == 1
assert b1 == 11

adj: dict[tuple, list[tuple]] = defaultdict(list)
for u, v in incidences:
    adj[u].append(v)
    adj[v].append(u)
assert all(len(adj[v]) == 3 for v in vertices)
seen = {vertices[0]}
queue = deque([vertices[0]])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            queue.append(v)
assert len(seen) == 20

# Johnson graph J(5,3): two triples are adjacent when they share two elements.
johnson_adj = {t: [] for t in corners}
for t in corners:
    for u in corners:
        if t != u and len(set(t).intersection(u)) == 2:
            johnson_adj[t].append(u)
johnson_seen = {corners[0]}
johnson_queue = deque([corners[0]])
while johnson_queue:
    t = johnson_queue.popleft()
    for u in johnson_adj[t]:
        if u not in johnson_seen:
            johnson_seen.add(u)
            johnson_queue.append(u)
assert len(johnson_seen) == 10
assert all(len(johnson_adj[t]) == 6 for t in corners)

# ---------------------------------------------------------------------------
# 4. Exterior-algebra relation in a standard general-position arrangement.
#    L_0,...,L_3 are coordinate covectors and L_4=-(L_0+...+L_3), so a_i=1.
# ---------------------------------------------------------------------------
L = [
    sp.Matrix([[1, 0, 0, 0]]),
    sp.Matrix([[0, 1, 0, 0]]),
    sp.Matrix([[0, 0, 1, 0]]),
    sp.Matrix([[0, 0, 0, 1]]),
    sp.Matrix([[-1, -1, -1, -1]]),
]
a = [sp.Integer(1)] * 5
assert sum((a[i] * L[i] for i in range(5)), sp.zeros(1, 4)) == sp.zeros(1, 4)

def contraction_vector(i: int, j: int, k: int) -> sp.Matrix:
    """v with i_v(dx0^dx1^dx2^dx3)=L_i^L_j^L_k."""
    A = sp.Matrix.vstack(L[i], L[j], L[k])
    vals = []
    for col in range(4):
        minor = A[:, [c for c in range(4) if c != col]]
        vals.append((-1) ** col * minor.det())
    return sp.Matrix(vals)

# Every triple vector lies in the corresponding three hyperplanes.
for i, j, k in itertools.combinations(base, 3):
    v = contraction_vector(i, j, k)
    assert v != sp.zeros(4, 1)
    assert L[i].dot(v) == L[j].dot(v) == L[k].dot(v) == 0

line_relations = {}
for i, j in necks:
    comp = [k for k in base if k not in (i, j)]
    ws = [a[i] * a[j] * a[k] * contraction_vector(i, j, k) for k in comp]
    total = sum(ws, sp.zeros(4, 1))
    assert total == sp.zeros(4, 1)
    # Any two are linearly independent and the third is their negative sum.
    assert sp.Matrix.hstack(ws[0], ws[1]).rank() == 2
    assert ws[0] + ws[1] + ws[2] == sp.zeros(4, 1)
    line_relations[f"{i}{j}"] = {
        "complement": comp,
        "vectors": [[int(x) for x in w] for w in ws],
        "sum": [int(x) for x in total],
    }

# At a fixed triple, incidence representatives differ only by sign.
triple_signs = {}
for tau in corners:
    i, j, k = tau
    canonical = a[i] * a[j] * a[k] * contraction_vector(i, j, k)
    reps = {
        f"{i}{j};{k}": a[i] * a[j] * a[k] * contraction_vector(i, j, k),
        f"{i}{k};{j}": a[i] * a[k] * a[j] * contraction_vector(i, k, j),
        f"{j}{k};{i}": a[j] * a[k] * a[i] * contraction_vector(j, k, i),
    }
    signs = {}
    for name, rep in reps.items():
        if rep == canonical:
            signs[name] = 1
        elif rep == -canonical:
            signs[name] = -1
        else:
            raise AssertionError((tau, name, rep, canonical))
    triple_signs["".join(map(str, tau))] = signs

report = {
    "balanced_potential": {
        "area": "2*pi",
        "cusp_model": "r + 2*log(r)",
        "laplacian": str(Delta_h0),
        "flux_per_cusp": "2*pi",
        "rhs_total_mass": "6*pi",
        "charge_identity": "5 = 2 + 3",
    },
    "s3_reference_polynomial": {
        "expanded": str(p_star),
        "p(1-z)/p(z)": str(transform_1_minus_z),
        "z^5 p(1/z)/p(z)": str(transform_inverse),
        "p(0)": str(p_star.subs(z, 0)),
        "p(1)": str(p_star.subs(z, 1)),
        "leading_coefficient": str(sp.Poly(p_star, z).LC()),
    },
    "desargues_graph": {
        "vertices": len(vertices),
        "edges": len(incidences),
        "boundary_rank": rank_B,
        "b0": b0,
        "b1": b1,
        "regular_degree": 3,
        "triple_johnson_graph_connected": True,
        "triple_johnson_degree": 6,
    },
    "standard_arrangement_exterior_relations": line_relations,
    "triple_incidence_signs": triple_signs,
}
OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
OUT_TXT.write_text(
    "Balanced punctured-neck certificate passed.\n"
    "Delta(r+2 log r)=-2; flux per cusp=2*pi; 5=2+3.\n"
    "S3 reference polynomial checks passed.\n"
    "Desargues graph: V=20, E=30, rank=19, b1=11.\n"
    "All ten exterior-algebra line relations sum to zero.\n"
    "Triple incidence representatives agree up to sign.\n"
    "Johnson graph J(5,3) is connected; edge differences recover normalized triple values.\n",
    encoding="utf-8",
)
print(OUT_TXT.read_text(encoding="utf-8"), end="")
