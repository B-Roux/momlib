# Graph Object Instance Methods

Expresses the mathematical notion of an undirected, optionally
    weighted graph in native Python datastructures and datatypes
    while providing an assortment of tools to perform basic graph
    manipulations.

`Graph` objects are considered mutable, which means they can be
    modified and should not be used as dictionary keys or set items.

## Contents

- [\_\_init\_\_](#__init__)
- [\_\_len\_\_](#__len__)
- [\_\_str\_\_](#__str__)
- [\_\_repr\_\_](#__repr__)
- [new\_node](#new_node)
- [get\_edge](#get_edge)
- [get\_neighbors](#get_neighbors)
- [set\_edge](#set_edge)
- [set\_neighbors](#set_neighbors)
- [degree](#degree)

---

# \_\_init\_\_

```python
(self, node_count: 'int' = 0, edges: 'Optional[Iterable[Iterable[float | Fraction | None]]]' = None) -> 'None'
```

Initializes a new instance of the `Graph` class.

Arguments
- node\_count: The number of nodes to initialize the graph with.
- edges: The edge data to initialize the graph with - an
    iterable that must produce a lower triangular matrix such
    that each entry describes a connection between the nodes
    that correspond to its coordinates.
    Using this parameter is not recommended, instead, consider
    using the `set\_neighbors` or `set\_edge` function.
    Optional, defaults to `None`.

Possible Errors
- ValueError: If `edges` produces a malformed lower triangular
    matrix.

---

# \_\_len\_\_

```python
(self) -> 'int'
```

Returns the total number of nodes in this graph.

---

# \_\_str\_\_

```python
(self) -> 'str'
```

Returns a "pretty" string representation of this graph.

---

# \_\_repr\_\_

```python
(self) -> 'str'
```

Returns a reproduction string representation of this graph.

Notes
- Assuming all relevant libraries have been imported, the
    reproduction string can be run as valid Python to create
    an exact copy of this graph.

---

# new\_node

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
    blank and calling the `set\_neighbors` method manually.

---

# get\_edge

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

# get\_neighbors

```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```

Generate neighbor index-weight tuples for each edge this node
    shares with a neighbor node.

Arguments
- node: The node for which to find neighbor nodes.

---

# set\_edge

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

# set\_neighbors

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

---

# degree

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

<!--this file has been automatically generated-->
