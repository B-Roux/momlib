"""
Provides graph theory objects and and tools.

Notes
- Node relations are consistently described with familial relations:
    - `neighbor` in an undirected graph refers to a node that shares an
        edge with the specified node.
    - `child` in a directed graph refers to a node that is the
        destination of an edge starting at the specified node.
    - `parent` in a directed graph refers to a node that is the
        source of an edge terminating at the specified node.
    - This does not, however, imply anything other than what has been
        specified above. A child node can be its own grandfather if its
        parent is also its child. For further information, the song
        "I'm My Own Grandpa" should be consulted.
"""

import warnings

from .header import NodeNotFoundError
from .graph import Graph
from .digraph import DiGraph


__all__ = (
    "NodeNotFoundError",
    "Graph",
    "DiGraph",
)


warnings.warn(
    "momlib.graph is still in very early development, expect code that relies on this module to break often (until this warning is removed when the module matures)",
    category=FutureWarning,
    stacklevel=3,
)
