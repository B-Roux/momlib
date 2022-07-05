"""
Provides graph theory objects and and tools.
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
