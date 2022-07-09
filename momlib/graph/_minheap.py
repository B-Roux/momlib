"""
Provides basic methods for implementing a min heap priority queue for
    internal use by the graph theory submodule.

Min heaps are implemented as lists that maintain the min heap property
    in-place.
"""

from fractions import Fraction

__all__ = (
    "build_min_heap",
    "extract_min",
    "decrease_key",
)


def build_min_heap(
    unsorted: list[tuple[int, Fraction | None]],
) -> None:
    """
    Converts an unsorted array into a min heap.
    """
    for i in range(len(unsorted) // 2, -1, -1):
        _min_heapify(unsorted, i)


def extract_min(
    heap: list[tuple[int, Fraction | None]],
) -> tuple[int, Fraction | None]:
    """
    Removes and returns the minimum element in a min heap.
    """
    min_el = heap[0]
    heap[0] = heap[-1]
    del heap[-1]
    _min_heapify(heap, 0)
    return min_el


def decrease_key(
    heap: list[tuple[int, Fraction | None]],
    index: int,
    key: Fraction,
) -> None:
    """
    Reduces the key value for a given item in the heap.
    """
    heap[index] = (heap[index][0], key)
    while index > 0 and _compare_frac_none(
        heap[index][1],
        heap[_parent(index)][1],
    ):
        heap[_parent(index)], heap[index] = (
            heap[index],
            heap[_parent(index)],
        )


def _compare_frac_none(
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


def _parent(
    i: int,
) -> int:
    """
    Returns a heap parent index.
    """
    return (i - 1) // 2


def _right_child(
    i: int,
) -> int:
    """
    Returns a heap right-child index.
    """
    return (i * 2) + 2


def _left_child(
    i: int,
) -> int:
    """
    Returns a heap left-child index.
    """
    return (i * 2) + 1


def _min_heapify(
    heap: list[tuple[int, Fraction | None]],
    i: int,
) -> None:
    """
    Maintains the min heap property for a given index in a heap.
    """
    lc = _left_child(i)
    rc = _right_child(i)
    if lc < len(heap) and _compare_frac_none(heap[lc][1], heap[i][1]):
        smallest = lc
    else:
        smallest = i
    if rc < len(heap) and _compare_frac_none(heap[rc][1], heap[smallest][1]):
        smallest = rc
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        _min_heapify(heap, smallest)
