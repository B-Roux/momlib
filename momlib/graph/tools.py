"""
This is a placeholder.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable

from .header import NegativeWeightError
from .graph import Graph
from .digraph import DiGraph

__all__ = ("shortest_paths",)


def shortest_paths(
    graph: Graph | DiGraph,
    source: int,
) -> tuple[list[float], list[int | None]]:
    def weight_to_float(x: Fraction | None) -> float:
        if x is None:
            return float("inf")
        elif x >= Fraction(0):
            return float(x)
        else:
            raise NegativeWeightError(
                "negative weight detected, cannot proceed"
            )

    distance: list[float] = [float("inf")] * len(graph)
    previous: list[int | None] = [None] * len(graph)
    queue: list[tuple[int, float]] = []

    distance[source] = 0
    queue.append((source, 0))

    for node in range(len(graph)):
        if node != source:
            distance[node] = float("inf")
            previous[node] = None
        queue.append((node, distance[node]))

    while len(queue) > 0:
        idx, parent = min(enumerate(queue), key=lambda x: x[1][1])
        del queue[idx]
        for child in _outgoing_edges(graph, parent[0]):
            alternate_path = distance[parent[0]] + weight_to_float(
                graph.get_edge(parent[0], child[0])
            )
            if (alternate_path < distance[child[0]]) and (
                distance[parent[0]] != float("inf")
            ):
                distance[child[0]] = alternate_path
                previous[child[0]] = parent[0]
                for idx, item in enumerate(queue):
                    if item[0] == child[0]:
                        queue[idx] = (child[0], alternate_path)
    return distance, previous


# PRIVATE/PROTECTED METHODS


def _outgoing_edges(
    graph: Graph | DiGraph,
    source: int,
) -> Iterable[tuple[int, Fraction]]:
    if isinstance(graph, Graph):
        return graph.get_neighbors(source)
    else:
        return graph.get_children(source)
