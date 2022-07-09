# Graph Object API

Expresses the mathematical notion of an undirected, optionally
    weighted graph in native Python datastructures and datatypes
    while providing an assortment of tools to perform basic graph
    manipulations.

`Graph` objects are considered mutable, which means they can be
    modified and should not be used as dictionary keys or set items.

## Contents

- [degree](#graphdegree)
- [get\_edge](#graphget\_edge)
- [get\_neighbors](#graphget\_neighbors)
- [new\_node](#graphnew\_node)
- [set\_edge](#graphset\_edge)
- [set\_neighbors](#graphset\_neighbors)

---

## Graph.degree
```python
(self, node: 'int') -> 'Fraction'
```
Calculates the degree of a node in this graph, where degree
    refers to the combined weight of all edges adjacent to the
    node.

Arguments
- node: The node for which to find the degree.

Notes
- For 'loop edges' (edges that start and end at the same node),
    the degree is counted twice. This is not a bug, it has to
    do with the definition of degree in an undirected graph.

---

## Graph.get\_edge
```python
(self, node: 'int', neighbor: 'int') -> 'Fraction | None'
```
Gets the value of an edge between two nodes.

Arguments
- node: The parent node of the edge.
- neighbor: The child node of the edge.

Possible Errors
- NodeNotFoundError: If a specified node index does not exist.

Notes
- Since undirected edges have no directionality, the order of
    the operands does not matter.

---

## Graph.get\_neighbors
```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```
Generate neighbor index-weight tuples for each edge this node
    shares with a neighbor node.

Arguments
- node: The node for which to find neighbor nodes.

---

## Graph.new\_node
```python
(self, neighbors: 'Optional[Iterable[int | tuple[int, float | Fraction | None]]]' = None) -> 'int'
```
Creates a new node in this graph, and returns its index for
    convenience.

Arguments
- neighbors: An iterable of node indices or index-weight tuples
    that will be used to initialize the new node's neighbors.
    Optional, defaults to none.

Notes
- Specifying the neighbors parameter is equivalent to leaving it
    blank and calling the `set_neighbors` method manually.

---

## Graph.set\_edge
```python
(self, node: 'int', neighbor: 'int', weight: 'float | Fraction | None' = Fraction(1, 1)) -> 'None'
```
Set the value of an edge by overwriting its old value.

Arguments
- node: The source node for the edge.
- neighbor: The destination node for the edge.
- weight: The weight of the edge.
    Optional, defaults to 1.

Possible Errors
- NodeNotFoundError: If a specified node index does not exist.

Notes
- A weight of 0 does not imply a non-connection, it simply means
    a connection with weight 0. To explicitly specify a
    non-connection, use a weight of `None`.
- Since undirected edges have no directionality, the order of
    the node index operands does not matter.

---

## Graph.set\_neighbors
```python
(self, node: 'int', neighbors: 'Iterable[int | tuple[int, float | Fraction | None]]') -> 'None'
```
Set edges based on indices or index-weight tuples for each edge
    this node shares with a neighbor node.

Arguments
- node: The node for which to set neighbor nodes.

Notes
- A weight of 0 does not imply a non-connection, it simply means
    a connection with weight 0. To explicitly specify a non-
    connection, use a weight of `None`.

<!--This file has been automatically generated-->
