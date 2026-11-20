#!/usr/bin/env python3
"""Orbit reduction and mesh certificate for the square complex C_5.

C_5 is the union of the 30 unit squares
    Q_{i;jk} = e_i + [0,1]e_j + [0,1]e_k
for distinct i,j,k in {0,...,4} and j<k, with its intrinsic square-complex
metric.  The script:

1. classifies unordered pairs of squares under S_5 (there are nine orbits);
2. builds the complete-in-each-cell 1/N mesh graph;
3. computes the maximum graph distance for one representative of each orbit;
4. applies the covering estimate
       sup_{x in S,y in T} d(x,y) <= M_N(S,T) + sqrt(2)/N.

Every graph edge is an actual straight segment in one square.  Hence graph
lengths are rigorous upper bounds for intrinsic distances between mesh points.
Floating-point Dijkstra is used, so this is a reproducible numerical certificate,
not an interval-arithmetic proof.  The gap eliminating the seven noncritical
orbits is much larger than roundoff.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

Cell = Tuple[int, int, int]
Coord = Tuple[int, int, int, int, int]
Pair = Tuple[int, int]


def cells() -> List[Cell]:
    ans: List[Cell] = []
    for triple in itertools.combinations(range(5), 3):
        for distinguished in triple:
            j, k = sorted(set(triple) - {distinguished})
            ans.append((distinguished, j, k))
    return ans


CELLS = cells()
CELL_INDEX = {cell: i for i, cell in enumerate(CELLS)}
PERMUTATIONS = list(itertools.permutations(range(5)))


def act_cell(cell_index: int, permutation: Sequence[int]) -> int:
    i, j, k = CELLS[cell_index]
    jj, kk = sorted((permutation[j], permutation[k]))
    return CELL_INDEX[(permutation[i], jj, kk)]


def canonical_unordered_pair(a: int, b: int) -> Pair:
    images: List[Pair] = []
    for permutation in PERMUTATIONS:
        aa = act_cell(a, permutation)
        bb = act_cell(b, permutation)
        images.append(tuple(sorted((aa, bb))))
    return min(images)


@dataclass(frozen=True)
class Orbit:
    canonical_pair: Pair
    representative: Pair
    size: int


def pair_orbits() -> List[Orbit]:
    buckets: Dict[Pair, List[Pair]] = {}
    for a in range(len(CELLS)):
        for b in range(a, len(CELLS)):
            key = canonical_unordered_pair(a, b)
            buckets.setdefault(key, []).append((a, b))

    ans: List[Orbit] = []
    for key, members in sorted(buckets.items()):
        representatives = [pair for pair in members if pair[0] == 0]
        if not representatives:
            raise RuntimeError(f"orbit {key} has no representative with first cell 0")
        ans.append(Orbit(key, representatives[0], len(members)))
    if len(ans) != 9 or sum(o.size for o in ans) != 465:
        raise RuntimeError("unexpected orbit count")
    return ans


def build_mesh_graph(nmesh: int) -> Tuple[List[Coord], List[List[int]], csr_matrix]:
    if nmesh < 1:
        raise ValueError("nmesh must be positive")

    point_id: Dict[Coord, int] = {}
    coordinates: List[Coord] = []
    cell_nodes: List[List[int]] = []

    for i, j, k in CELLS:
        nodes: List[int] = []
        for a in range(nmesh + 1):
            for b in range(nmesh + 1):
                coord = [0] * 5
                coord[i] = nmesh
                coord[j] = a
                coord[k] = b
                key: Coord = tuple(coord)  # type: ignore[assignment]
                if key not in point_id:
                    point_id[key] = len(coordinates)
                    coordinates.append(key)
                nodes.append(point_id[key])
        cell_nodes.append(nodes)

    edge_weight: Dict[Tuple[int, int], float] = {}
    for nodes in cell_nodes:
        array = np.asarray([coordinates[node] for node in nodes], dtype=float) / nmesh
        for p, u in enumerate(nodes):
            differences = array[p + 1 :] - array[p]
            weights = np.sqrt(np.sum(differences * differences, axis=1))
            for q, weight in enumerate(weights, start=p + 1):
                v = nodes[q]
                edge = (u, v) if u < v else (v, u)
                old = edge_weight.get(edge)
                if old is None or weight < old:
                    edge_weight[edge] = float(weight)

    rows: List[int] = []
    columns: List[int] = []
    data: List[float] = []
    for (u, v), weight in edge_weight.items():
        rows.extend((u, v))
        columns.extend((v, u))
        data.extend((weight, weight))

    graph = csr_matrix(
        (data, (rows, columns)),
        shape=(len(coordinates), len(coordinates)),
        dtype=float,
    )
    return coordinates, cell_nodes, graph


def local_mesh_coordinates(index: int, nmesh: int) -> Tuple[int, int]:
    return divmod(index, nmesh + 1)


def recognize_square(value: float) -> str:
    candidates = {
        2: r"sqrt(2)",
        5: r"sqrt(5)",
        8: r"2sqrt(2)",
        10: r"sqrt(10)",
        13: r"sqrt(13)",
    }
    squared = value * value
    nearest = min(candidates, key=lambda n: abs(squared - n))
    if abs(squared - nearest) < 5e-10:
        return candidates[nearest]
    return f"{value:.12g}"


def run(nmesh: int, csv_path: Path | None) -> None:
    orbits = pair_orbits()
    coordinates, cell_nodes, graph = build_mesh_graph(nmesh)
    source_nodes = cell_nodes[0]
    distances = dijkstra(
        graph,
        directed=False,
        indices=source_nodes,
        return_predecessors=False,
    )

    target = math.sqrt(13.0)
    cover_error = math.sqrt(2.0) / nmesh
    rows_for_csv: List[dict[str, object]] = []

    print(f"N={nmesh}; vertices={len(coordinates)}; undirected edges={graph.nnz // 2}")
    print(f"covering error sqrt(2)/N = {cover_error:.12f}")
    print()
    header = (
        "orbit  size  representative                    M_N             "
        "M_N+sqrt(2)/N   bad mesh pairs"
    )
    print(header)
    print("-" * len(header))

    for orbit_number, orbit in enumerate(orbits, start=1):
        source, target_cell = orbit.representative
        if source != 0:
            raise RuntimeError("representative must start with cell 0")
        block = distances[:, cell_nodes[target_cell]]
        maximum = float(np.max(block))
        upper = maximum + cover_error
        bad = np.argwhere(block + cover_error > target + 1e-12)

        source_box = ""
        target_box = ""
        if len(bad):
            source_ab = np.asarray(
                [local_mesh_coordinates(int(i), nmesh) for i, _ in bad], dtype=int
            )
            target_ab = np.asarray(
                [local_mesh_coordinates(int(j), nmesh) for _, j in bad], dtype=int
            )
            source_box = (
                f"[{source_ab[:,0].min()},{source_ab[:,0].max()}]x"
                f"[{source_ab[:,1].min()},{source_ab[:,1].max()}]"
            )
            target_box = (
                f"[{target_ab[:,0].min()},{target_ab[:,0].max()}]x"
                f"[{target_ab[:,1].min()},{target_ab[:,1].max()}]"
            )

        rep_text = f"Q{source}={CELLS[source]}, Q{target_cell}={CELLS[target_cell]}"
        print(
            f"{orbit_number:>2}    {orbit.size:>3}  {rep_text:<34} "
            f"{recognize_square(maximum):>10}={maximum:.9f}  "
            f"{upper:.9f}       {len(bad):>5}"
        )

        rows_for_csv.append(
            {
                "orbit": orbit_number,
                "orbit_size": orbit.size,
                "source_cell_index": source,
                "source_cell": str(CELLS[source]),
                "target_cell_index": target_cell,
                "target_cell": str(CELLS[target_cell]),
                "mesh_max_distance": f"{maximum:.15f}",
                "recognized_value": recognize_square(maximum),
                "cover_error": f"{cover_error:.15f}",
                "certified_upper": f"{upper:.15f}",
                "bad_mesh_pair_count": len(bad),
                "bad_source_local_index_box": source_box,
                "bad_target_local_index_box": target_box,
            }
        )

    global_upper = target + cover_error
    print()
    print(f"rigorous geometric bracket modulo floating roundoff:")
    print(f"  sqrt(13) <= diam(C_5) <= sqrt(13)+sqrt(2)/N = {global_upper:.12f}")
    print("Seven orbits are eliminated outright; only representatives Q0-Q16 and Q0-Q25 remain critical.")

    if csv_path is not None:
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        with csv_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows_for_csv[0].keys()))
            writer.writeheader()
            writer.writerows(rows_for_csv)
        print(f"wrote {csv_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--nmesh",
        type=int,
        default=12,
        help="mesh denominator (12 is fast; 18 uses roughly 0.6 GB RAM)",
    )
    parser.add_argument("--csv", type=Path, default=None, help="optional CSV output")
    args = parser.parse_args()
    run(args.nmesh, args.csv)


if __name__ == "__main__":
    main()
