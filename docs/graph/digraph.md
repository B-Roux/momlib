# DiGraph Object Instance Methods

Expresses the mathematical notion of a directed, optionally
    weighted graph in native Python datastructures and datatypes
    while providing an assortment of tools to perform basic graph
    manipulations.

`DiGraph` objects are considered mutable, which means they can be
    modified and should not be used as dictionary keys or set items.

## Contents

- [\_\_init\_\_](#__init__)
- [\_\_len\_\_](#__len__)
- [\_\_str\_\_](#__str__)
- [\_\_repr\_\_](#__repr__)
- [new\_node](#new_node)
- [get\_edge](#get_edge)
- [get\_parents](#get_parents)
- [get\_children](#get_children)
- [set\_edge](#set_edge)
- [set\_parents](#set_parents)
- [set\_children](#set_children)
- [indegree](#indegree)
- [outdegree](#outdegree)

---

# \_\_init\_\_

```python
(self, node_count: 'int' = 0, edges: 'Optional[Iterable[Iterable[float | Fraction | None]]]' = None) -> 'None'
```

Initializes a new instance of the `DiGraph` class.

Arguments
- node\_count: The number of nodes to initialize the digraph
    with.
- edges: The edge data to initialize the digraph with - an
    iterable that must produce a matrix such that each entry
    describes a connection between the nodes that correspond to
    its coordinates.
    Using this parameter is not recommended, instead, consider
    using the `set\_children`, `set\_parents` or `set\_edge`
    functions.
    Optional, defaults to `None`.

Possible Errors
- ValueError: If `edges` produces a malformed adjacency matrix.

---

# \_\_len\_\_

```python
(self) -> 'int'
```

Returns the total number of nodes in this digraph.

---

# \_\_str\_\_

```python
(self) -> 'str'
```

Returns a "pretty" string representation of this digraph.

---

# \_\_repr\_\_

```python
(self) -> 'str'
```

Returns a reproduction string representation of this digraph.

Notes
- Assuming all relevant libraries have been imported, the
    reproduction string can be run as valid Python to create
    an exact copy of this digraph.

---

# new\_node

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
    leaving it blank and calling the `set\_children` or
    `set\_parents` methods (respectively) manually.

---

# get\_edge

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

# get\_parents

```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```

Generate index-weight tuples for each edge from this a parent
    node to this node.

Arguments
- node: The node for which to find parent nodes.

---

# get\_children

```python
(self, node: 'int') -> 'Iterable[tuple[int, Fraction]]'
```

Generate index-weight tuples for each edge from this node to a
    child node.

Arguments
- node: The node for which to find child nodes.

---

# set\_edge

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

# set\_parents

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

---

# set\_children

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

# indegree

```python
(self, node: 'int') -> 'Fraction'
```

Calculates the in-degree of a node in this digraph, where
    in-degree refers to the combined weight of all incoming to
    the node.

Arguments
- node: The node for which to find the in-degree.

---

# outdegree

```python
(self, node: 'int') -> 'Fraction'
```

Calculates the out-degree of a node in this digraph, where
    out-degree refers to the combined weight of all outgoing
    edges from the node.

Arguments
- node: The node for which to find the out-degree.

<!--this file has been automatically generated-->
