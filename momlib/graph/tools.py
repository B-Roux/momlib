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
) -> tuple[list[Fraction | None], list[int | None]]:

    distance: list[Fraction | None] = [None] * len(graph)
    previous: list[int | None] = [None] * len(graph)
    queue: list[tuple[int, Fraction | None]] = []

    def join_weights(
        parent: Fraction | None, child: Fraction | None
    ) -> Fraction | None:
        if parent is None or child is None:
            return None
        elif parent < 0 or child < 0:
            raise NegativeWeightError(
                "cannot compute the shortest path of a graph with negative"
                "weights"
            )
        else:
            return parent + child

    distance[source] = Fraction(0)
    queue.append((source, Fraction(0)))

    for node in range(len(graph)):
        queue.append((node, distance[node]))

    while len(queue) > 0:
        idx, (parent, _) = min(
            enumerate(queue),
            key=lambda x: (
                float(x[1][1]) if x[1][1] is not None else float("inf")
            ),
        )
        del queue[idx]
        for child, _ in _outgoing_edges(graph, parent):

            alternate_path = join_weights(
                distance[parent], graph.get_edge(parent, child)
            )
            child_min_distance = distance[child]
            if alternate_path is not None and (
                (child_min_distance is None)
                or (alternate_path < child_min_distance)
            ):
                distance[child] = alternate_path
                previous[child] = parent
                for idx, (item, _) in enumerate(queue):
                    if item == child:
                        queue[idx] = (child, alternate_path)
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
