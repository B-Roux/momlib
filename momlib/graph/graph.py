"""
Implements the `Graph` class (see `help(Graph)`).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import chain
from typing import Iterable, Optional

from .header import NodeNotFoundError

from ..linalg import Matrix

__all__ = ("Graph",)


class Graph:
    """
    This is a placeholder.
    """

    __slots__ = ("_edge_data", "_length")

    def __init__(
        self,
        node_count: int = 0,
        edges: Optional[Iterable[Iterable[float | Fraction | None]]] = None,
    ) -> None:
        """
        This is a placeholder.
        """
        edge_data: list[list[Fraction | None]] | None = None
        if edges is not None:
            edge_data = [
                [Fraction(item) if item is not None else None for item in row]
                for row in edges
            ]
            if len(edge_data) != node_count:
                raise ValueError("node count and edge data dimension mismatch")
            for index, edge_data_row in enumerate(edge_data):
                if len(edge_data_row) != index + 1:
                    raise ValueError(
                        "node count and edge data dimension mismatch"
                    )
        else:
            edge_data = [
                [None for _ in range(i + 1)] for i in range(node_count)
            ]
        self._edge_data: list[list[Fraction | None]] = edge_data
        self._length: int = node_count

    def __len__(
        self,
    ) -> int:
        """
        This is a placeholder.
        """
        return self._length

    def __str__(
        self,
    ) -> str:
        """
        This is a placeholder.
        """
        graph_string_builder: list[str | None] = [
            None for _ in range(self._length)
        ]
        for node in range(self._length):
            node_name = f"{node} \u25c1\u2500"
            node_name_space = " " * len(node_name)
            neighbors = list(self.get_neighbors(node))
            num_neighbors = len(neighbors)
            node_string_builder: list[str | None] = [
                None for _ in range(num_neighbors)
            ]
            for i in range(num_neighbors):
                if i == 0:
                    if num_neighbors == 1:
                        node_string_builder[i] = (
                            f"{node_name}\u2500\u2500({neighbors[i][1]})"
                            f"\u2500\u25b7 {neighbors[i][0]}"
                        )
                    else:
                        node_string_builder[i] = (
                            f"{node_name}\u252c\u2500({neighbors[i][1]})"
                            f"\u2500\u25b7 {neighbors[i][0]}"
                        )
                elif i == num_neighbors - 1:
                    node_string_builder[i] = (
                        f"{node_name_space}\u2514\u2500({neighbors[i][1]})"
                        f"\u2500\u25b7 {neighbors[i][0]}"
                    )
                else:
                    node_string_builder[i] = (
                        f"{node_name_space}\u251c\u2500({neighbors[i][1]})"
                        f"\u2500\u25b7 {neighbors[i][0]}"
                    )
            graph_string_builder[node] = "\n".join(
                s for s in node_string_builder if s is not None
            )
            if graph_string_builder[node] == "":
                graph_string_builder[node] = None
        return "\n\n".join(s for s in graph_string_builder if s is not None)

    def __repr__(
        self,
    ) -> str:
        """
        This is a placeholder.
        """
        obj_name = self.__class__.__name__
        node_count = self._length
        edge_data = "[\n        [{}],\n    ]".format(
            "],\n        [".join(
                ", ".join(repr(item) for item in row)
                for row in self._edge_data
            )
        )
        return (
            f"{obj_name}(\n"
            f"    node_count={node_count},\n"
            f"    edge_data={edge_data},\n"
            f")"
        )

    def new_node(
        self,
        neighbors: Optional[
            Iterable[int | tuple[int, float | Fraction | None]]
        ] = None,
    ) -> int:
        """
        This is a placeholder.
        """
        new_node_index = self._length
        self._length += 1
        self._edge_data.append([None] * self._length)
        if neighbors is not None:
            self.set_neighbors(new_node_index, neighbors)
        return new_node_index

    def get_edge(
        self,
        node: int,
        neighbor: int,
    ) -> Fraction | None:
        """
        This is a placeholder.
        """
        try:
            if node > neighbor:
                return self._edge_data[node][neighbor]
            else:
                return self._edge_data[neighbor][node]
        except IndexError:
            raise NodeNotFoundError(
                f"could not find edge from {node} to {neighbor}"
            )

    def get_neighbors(
        self,
        node: int,
    ) -> Iterable[tuple[int, Fraction]]:
        """
        This is a placeholder.
        """
        for i in range(self._length):
            weight = self.get_edge(node, i)
            if weight is not None:
                yield i, weight

    def set_edge(
        self,
        node: int,
        neighbor: int,
        weight: float | Fraction | None = Fraction(1),
    ) -> None:
        """
        This is a placeholder.
        """
        try:
            if node > neighbor:
                if weight is None:
                    self._edge_data[node][neighbor] = None
                else:
                    self._edge_data[node][neighbor] = Fraction(weight)
            else:
                if weight is None:
                    self._edge_data[neighbor][node] = None
                else:
                    self._edge_data[neighbor][node] = Fraction(weight)
        except IndexError:
            raise NodeNotFoundError(
                f"could not find edge ({node}, {neighbor})"
            )

    def set_neighbors(
        self,
        node: int,
        neighbors: Iterable[int | tuple[int, float | Fraction | None]],
    ) -> None:
        """
        This is a placeholder.
        """
        for neighbor in neighbors:
            if isinstance(neighbor, int):
                self.set_edge(node, neighbor, Fraction(1))
            else:
                self.set_edge(node, neighbor[0], neighbor[1])

    def degree(
        self,
        node: int,
    ) -> Fraction:
        """
        This is a placeholder.
        """
        return sum(
            chain(
                (v for v in self._edge_data[node] if v is not None),
                (
                    v
                    for v in (
                        self._edge_data[i][node]
                        for i in range(node, self._length)
                    )
                    if v is not None
                ),
            ),
            start=Fraction(0),
        )

    # PROPERTIES

    @property
    def adjacency_matrix(
        self,
    ) -> Matrix:
        return Matrix(
            (
                item if item is not None else Fraction(0)
                for item in (self.get_edge(i, j) for j in range(self._length))
            )
            for i in range(self._length)
        )

    @property
    def degree_matrix(
        self,
    ) -> Matrix:
        return Matrix(
            (
                self.degree(i) if i == j else Fraction(0)
                for j in range(self._length)
            )
            for i in range(self._length)
        )
