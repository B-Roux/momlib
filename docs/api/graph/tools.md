# Graph Theory Methods

Provides an assortment of more advanced tools to work with `Graph` and
    `DiGraph` objects.

## Contents

- [shortest\_paths](#shortest\_paths)

---

## shortest\_paths
```python
(graph: 'Graph | DiGraph', source: 'int') -> 'tuple[list[Fraction | None], list[int | None]]'
```
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

<!--This file has been automatically generated-->
