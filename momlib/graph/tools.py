"""
This is a placeholder.
"""

from __future__ import annotations

from fractions import Fraction

from .graph import Graph
from .digraph import DiGraph

__all__ = ("shortest_path",)


def shortest_path(
    graph: Graph | DiGraph,
    start_node: int,
) -> list[int]:
    ...  # TODO


# PRIVATE/PROTECTED METHODS


def _frontier(graph: Graph | DiGraph, node: int) -> dict[int, Fraction]:
    if isinstance(graph, Graph):
        return graph.get_neighbors(node)
    else:
        return graph.get_children(node)
