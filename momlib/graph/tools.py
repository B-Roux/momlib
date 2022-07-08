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
    """
    Apply Dijkstra's algorithm to a graph to compute the shortest path
        from a source node to any other node. The first list returned
        will be the minimum distance between the node and the node
        that corresponds to a given index, while the second list
        returned will be the parent node of any node corresponding to a
        given index such that recursively following this path will
        lead to the source node.

    Arguments
    - graph: The graph for which to compute the shortest paths.
    - source: The "starting" node.

    Possible Errors
    - NegativeWeightError: If a negative weight is found.
    """
    # I wrote most of this while delirious with COVID-19, I'm sorry future me
    distance: list[Fraction | None] = [None] * len(graph)
    previous: list[int | None] = [None] * len(graph)
    queue: list[tuple[int, Fraction | None]] = []

    distance[source] = Fraction(0)
    for node in range(len(graph)):
        queue.append((node, distance[node]))
    _heap_build_min(queue)

    while len(queue) > 0:
        parent, _ = _heap_extract_min(queue)
        for child_node, child_distance in _outgoing_edges(graph, parent):
            if child_distance < 0:
                raise NegativeWeightError(
                    "cannot compute the shortest path of a graph with "
                    "negative weights"
                )
            parent_distance = distance[parent]
            if parent_distance is None:
                alternate_path = None
            else:
                alternate_path = parent_distance + child_distance
            child_current_path = distance[child_node]
            if alternate_path is not None and (
                (child_current_path is None)
                or (alternate_path < child_current_path)
            ):
                distance[child_node] = alternate_path
                previous[child_node] = parent
                for idx, (item, _) in enumerate(queue):
                    if item == child_node:
                        _heap_decrease_key(queue, idx, alternate_path)
    return distance, previous


# PRIVATE/PROTECTED METHODS


def _outgoing_edges(
    graph: Graph | DiGraph,
    source: int,
) -> Iterable[tuple[int, Fraction]]:
    """
    Finds the outgoing edges from a node in either a directed or
        undirected graph.
    """
    if isinstance(graph, Graph):
        return graph.get_neighbors(source)
    else:
        return graph.get_children(source)


# MIN HEAP METHODS


def _lt_frac_none(
    a: Fraction | None,
    b: Fraction | None,
) -> bool:
    """
    Compares two fractions or none values, where none is considered
        infinite (or greater than any non-none value).
    """
    if a is None:
        return False
    else:
        if b is None:
            return True
        else:
            return a < b


def _heap_parent(
    i: int,
):
    """
    Returns a heap parent index.
    """
    return (i - 1) // 2


def _heap_rchild(
    i: int,
):
    """
    Returns a heap right-child index.
    """
    return (i * 2) + 2


def _heap_lchild(
    i: int,
):
    """
    Returns a heap left-child index.
    """
    return (i * 2) + 1


def _heap_minify(
    heap: list[tuple[int, Fraction | None]],
    i: int,
):
    """
    Maintains the min heap property for a given index in a heap.
    """
    lc = _heap_lchild(i)
    rc = _heap_rchild(i)
    if lc < len(heap) and _lt_frac_none(heap[lc][1], heap[i][1]):
        smallest = lc
    else:
        smallest = i
    if rc < len(heap) and _lt_frac_none(heap[rc][1], heap[smallest][1]):
        smallest = rc
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        _heap_minify(heap, smallest)


def _heap_build_min(
    heap: list[tuple[int, Fraction | None]],
):
    """
    Converts an unsorted array into a min heap.
    """
    for i in range(len(heap) // 2, -1, -1):
        _heap_minify(heap, i)


def _heap_extract_min(
    heap: list[tuple[int, Fraction | None]],
):
    """
    Removes and returns the minimum element in a min heap.
    """
    min_el = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    _heap_minify(heap, 0)
    return min_el


def _heap_decrease_key(
    heap: list[tuple[int, Fraction | None]],
    index: int,
    key: Fraction,
):
    """
    Reduces the key value for a given item in the heap.
    """
    heap[index] = (heap[index][0], key)
    while index > 0 and _lt_frac_none(
        heap[index][1],
        heap[_heap_parent(index)][1],
    ):
        heap[_heap_parent(index)], heap[index] = (
            heap[index],
            heap[_heap_parent(index)],
        )
