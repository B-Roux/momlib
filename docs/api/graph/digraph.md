# Directed Graph Object API

Expresses the mathematical notion of an directed, optionally
    weighted graph in native Python datastructures and datatypes
    while providing an assortment of tools to perform basic graph
    manipulations.

`DiGraph` objects are considered mutable, which means they can be
    modified and should not be used as dictionary keys or set items.

## Contents

- [get\_children](#digraphget\_children)
- [get\_edge](#digraphget\_edge)
- [get\_parents](#digraphget\_parents)
- [indegree](#digraphindegree)
- [new\_node](#digraphnew\_node)
- [outdegree](#digraphoutdegree)
- [set\_children](#digraphset\_children)
- [set\_edge](#digraphset\_edge)
- [set\_parents](#digraphset\_parents)

---

## DiGraph.get\_children
```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```
Generate index-weight tuples for each edge from this node to a
    child node.

Arguments
- node: The node for which to find child nodes.

---

## DiGraph.get\_edge
```python
(self, parent: 'int', child: 'int') -> 'Fraction | None'
```
Gets the value of an edge from a parent to a child node.

Arguments
- parent: The parent node of the edge.
- child: The child node of the edge.

Possible Errors
- NodeNotFoundError: If a specified node index does not exist.

Notes
- Since directed edges have directionality, the order of the
    operands matters.

---

## DiGraph.get\_parents
```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```
Generate index-weight tuples for each edge from this a parent
    node to this node.

Arguments
- node: The node for which to find parent nodes.

---

## DiGraph.indegree
```python
(self, node: 'int') -> 'Fraction'
```
Calculates the in-degree of a node in this digraph, where
    in-degree refers to the combined weight of all incoming to
    the node.

Arguments
- node: The node for which to find the in-degree.

---

## DiGraph.new\_node
```python
(self, children: 'Optional[Iterable[int | tuple[int, float | Fraction | None]]]' = None, parents: 'Optional[Iterable[int | tuple[int, float | Fraction | None]]]' = None) -> 'int'
```
Creates a new node in this digraph, and returns its index for
    convenience.

Arguments
- children: An iterable of node indices or index-weight tuples
    that will be used to initialize the new node's outbound
    connections.
    Optional, defaults to none.
- parents: An iterable of node indices or index-weight tuples
    that will be used to initialize the new node's inbound
    connections.
    Optional, defaults to none.

Notes
- Specifying the children or parents parameters is equivalent to
    leaving it blank and calling the `set_children` or
    `set_parents` methods (respectively) manually.

---

## DiGraph.outdegree
```python
(self, node: 'int') -> 'Fraction'
```
Calculates the out-degree of a node in this digraph, where
    out-degree refers to the combined weight of all outgoing
    edges from the node.

Arguments
- node: The node for which to find the out-degree.

---

## DiGraph.set\_children
```python
(self, node: 'int', children: 'Iterable[int | tuple[int, float | Fraction | None]]') -> 'None'
```
Set edges based on indices or index-weight tuples for each edge
    from this node to a child node.

Arguments
- node: The node for which to set child nodes.

Notes
- A weight of 0 does not imply a non-connection, it simply means
    a connection with weight 0. To explicitly specify a non-
    connection, use a weight of `None`.

---

## DiGraph.set\_edge
```python
(self, parent: 'int', child: 'int', weight: 'float | Fraction | None' = Fraction(1, 1)) -> 'None'
```
Set the value of an edge by overwriting its old value.

Arguments
- parent: The source node for the edge.
- child: The destination node for the edge.
- weight: The weight of the edge.
    Optional, defaults to 1.

Possible Errors
- NodeNotFoundError: If a specified node index does not exist.

Notes
- A weight of 0 does not imply a non-connection, it simply means
    a connection with weight 0. To explicitly specify a
    non-connection, use a weight of `None`.
- Since directed edges have directionality, the order of the
    operands matters.

---

## DiGraph.set\_parents
```python
(self, node: 'int', parents: 'Iterable[int | tuple[int, float | Fraction | None]]') -> 'None'
```
Set edges based on indices or index-weight tuples for each edge
    from a parent node to a this node.

Arguments
- node: The node for which to set parent nodes.

Notes
- A weight of 0 does not imply a non-connection, it simply means
    a connection with weight 0. To explicitly specify a non-
    connection, use a weight of `None`.

<!--This file has been automatically generated-->
