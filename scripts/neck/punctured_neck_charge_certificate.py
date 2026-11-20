#!/usr/bin/env python3
"""Exact/symbolic checks for the punctured-neck charge and scale bookkeeping."""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from itertools import combinations
from pathlib import Path

import sympy as sp


@dataclass(frozen=True)
class Certificate:
    quintic_normal_degrees: tuple[int, int]
    quintic_triple_degree: int
    quintic_source_degree: int
    quintic_charge_balance: int
    general_degree_identity: str
    log_canonical_degree: str
    self_matching_degrees: list[int]
    double_lines: int
    triple_points: int
    sources: int
    cusp_incidences_from_edges: int
    cusp_incidences_from_triangles: int
    arcsinh_limit: str
    polynomial_depth_limit: str


def main() -> None:
    d = sp.symbols("d", integer=True, positive=True)
    charge_general = sp.simplify(1 + 1 + (d - 2) - d)
    assert charge_general == 0

    self_matching = [n for n in range(1, 30) if n - 4 == 1]
    assert self_matching == [5]

    vertices = range(5)
    edges = list(combinations(vertices, 2))
    triangles = list(combinations(vertices, 3))
    assert len(edges) == 10 and len(triangles) == 10
    edge_triangle_incidences = sum(
        1 for e in edges for tri in triangles if set(e).issubset(tri)
    )
    triangle_edge_incidences = sum(
        1 for tri in triangles for e in edges if set(e).issubset(tri)
    )
    assert edge_triangle_incidences == triangle_edge_incidences == 30

    L = sp.symbols("L", positive=True)
    arcsinh_limit = sp.limit(sp.asinh(L) - sp.log(L), L, sp.oo)
    assert sp.simplify(arcsinh_limit - sp.log(2)) == 0

    A = sp.symbols("A", positive=True)
    poly_limit = sp.limit(sp.log(L + 2 * A * sp.log(L)) - sp.log(L), L, sp.oo)
    assert poly_limit == 0

    cert = Certificate(
        quintic_normal_degrees=(1, 1),
        quintic_triple_degree=3,
        quintic_source_degree=5,
        quintic_charge_balance=1 + 1 + 3 - 5,
        general_degree_identity=str(charge_general),
        log_canonical_degree="d-4",
        self_matching_degrees=self_matching,
        double_lines=len(edges),
        triple_points=len(triangles),
        sources=len(edges) * 5,
        cusp_incidences_from_edges=edge_triangle_incidences,
        cusp_incidences_from_triangles=triangle_edge_incidences,
        arcsinh_limit=str(arcsinh_limit),
        polynomial_depth_limit=str(poly_limit),
    )

    out_json = Path("punctured_neck_charge_certificate.json")
    out_txt = Path("punctured_neck_charge_certificate.txt")
    out_json.write_text(json.dumps(asdict(cert), ensure_ascii=False, indent=2) + "\n")
    out_txt.write_text(
        "Punctured-neck charge certificate passed.\n"
        "quintic: 1+1+3-5=0; ten necks, fifty sources, thirty cusp incidences.\n"
        "degree-d self-matching occurs only for d=5.\n"
        "asinh(L)-log(L) -> log(2); polynomial source depths are first-scale invisible.\n"
    )
    print(out_txt.read_text(), end="")


if __name__ == "__main__":
    main()
