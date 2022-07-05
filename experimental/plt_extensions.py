from typing import List, Tuple
import matplotlib
import matplotlib.pyplot as plt
from math import sin, cos, pi
from random import random

from momlib.graph import Graph
from momlib.linalg import Matrix, Vector, matcat

__all__ = [
    "diagram",
]


def diagram(
    momlib_objects: Graph | Matrix | Vector,
    title: str | None = None,
    font_family: str = "monospace",
    zero_indexed: bool = True,
) -> None:
    matplotlib.rcParams["font.family"] = font_family
    if isinstance(momlib_objects, Graph):
        _graph(momlib_objects, zero_indexed)
    elif isinstance(momlib_objects, Matrix):
        _matrix(momlib_objects, zero_indexed)
    elif isinstance(momlib_objects, Vector):  # type: ignore
        _matrix(matcat(momlib_objects, column_wise=False), zero_indexed)
    if title is not None:
        plt.title(title)
    plt.show()


def _graph(graph: Graph, zero_indexed: bool) -> None:
    def parametric_circle(t: float, r: float = 1) -> Tuple[float, float]:
        return (r * cos(t * 2 * pi - pi / 2), -r * sin(t * 2 * pi - pi / 2))

    plt.xlim(-1.25, 1.25)
    plt.ylim(-1.25, 1.25)
    plt.axis("equal")
    plt.axis("off")

    num_nodes = len(graph)
    for node in range(num_nodes):
        for neighbor, weight in graph.get_neighbors(node).items():
            label_center = None
            if neighbor < node:
                start = parametric_circle(node / num_nodes)
                end = parametric_circle(neighbor / num_nodes)
                plt.plot((start[0], end[0]), (start[1], end[1]), "k-")
                rfrac = (random() * 0.7) + 0.15
                rfracr = 1 - rfrac
                label_center = (
                    (start[0] * rfrac + end[0] * rfracr),
                    (start[1] * rfrac + end[1] * rfracr),
                )
                plt.text(  # type: ignore
                    label_center[0],
                    label_center[1],
                    "%.3G" % float(weight),
                    color="k",
                    bbox={
                        "boxstyle": "circle",
                        "facecolor": "white",
                        "edgecolor": "black",
                        "alpha": 1,
                        "pad": 0.125,
                    },
                    ha="center",
                    va="center",
                )
            elif neighbor == node:
                size = 0.1
                resolution = 20
                center = parametric_circle(node / num_nodes, 1 + size)
                circle_x: List[float] = []
                circle_y: List[float] = []
                for i in range(resolution + 1):
                    c_point = parametric_circle(i / resolution, size)
                    circle_x.append(center[0] + c_point[0])
                    circle_y.append(center[1] + c_point[1])
                plt.plot(circle_x, circle_y, "k-")
                label_center = parametric_circle(
                    node / num_nodes, 1 + size * 2
                )
                plt.text(  # type: ignore
                    label_center[0],
                    label_center[1],
                    "%.3G" % float(weight),
                    color="k",
                    bbox={
                        "boxstyle": "circle",
                        "facecolor": "white",
                        "edgecolor": "black",
                        "alpha": 1,
                        "pad": 0.125,
                    },
                    ha="center",
                    va="center",
                )
        x, y = parametric_circle(node / num_nodes)
        plt.text(  # type: ignore
            x,
            y,
            str(node + (0 if zero_indexed else 1)),
            color="w",
            weight="bold",
            bbox={
                "boxstyle": "circle",
                "color": "black",
                "alpha": 1,
                "pad": 0.5,
            },
            ha="center",
            va="center",
        )


def _matrix(matrix: Matrix, zero_indexed: bool) -> None:
    element_list = [[float(item) for item in row] for row in matrix.rows]
    plt.matshow(  # type: ignore
        element_list,  # type: ignore
        cmap="gray",
        extent=(
            None
            if zero_indexed
            else (0.5, matrix.shape[1] + 0.5, matrix.shape[0] + 0.5, 0.5)
        ),
    )
    plt.colorbar()
