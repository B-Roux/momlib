# Graph Theory in MOMLib

Using the `momlib.graph` submodule.

---

A graph is a mathematical structure that can be described as a collection of nodes (or vertices) and connecting edges. MOMLib currently implements two graph objects: `Graph` for basic undirected and optionally weighted graphs, and `DiGraph` for basic directed and optionally weighted graphs. In addition to these objects, the `momlib.graph` submodule gives you several basic tools to work with graphs.

## Graphs

To make a new graph, first import the relevant module, optionally with an alias so that you're not stuck typing out the whole thing every time:

```python
import momlib.graph as gr
```

Now you can simply call the initializer function:

```python
my_graph = gr.Graph(5)
```

This call will initialize a graph with a given number of nodes, and with no edges connecting them (yet). You can quickly see the number of nodes in any given graph by calling `len(my_graph)`.

To start adding edges, we can use one of several different methods. The most straight forward would be the `set_edge` function:

```python
my_graph.set_edge(0, 1)
my_graph.set_edge(0, 2)
my_graph.set_edge(1, 2, 2) #Set edge with a weight of 2
my_graph.set_edge(2, 3)
my_graph.set_edge(1, 4)
```

Note that:

- The edges are numbered starting from 0, so a `Graph` of length 5 will have edges 0 to 4.
- We can specify a weight as an optional 3rd argument to the `set_edge` function.

Now, if we realized we wanted a sixth node, we can create a new node on the graph with the `new_node` function:

```python
my_graph.new_node()
```

Notice the `neighbors` parameter: this iterable of integers (or integer-real number tuples if we want to specify the weights) can be used to very quickly initialize the edges a node shares with its neighbors - so instead of calling the above function, if we wanted the 6th node to connect to every other node, we can do this:

```python
my_graph.new_node(range(5))
```

Alternatively, if the node has already been created, we can use the `set_neighbors(<node number>, <neighbors>)` function to accomplish exactly the same task.

Now at this point, we may want to start getting a look at what the graph actually looks like:

```python
print(my_graph)
```
```
0 ◁─┬─(1)─▷ 1
    ├─(1)─▷ 2
    └─(1)─▷ 5

1 ◁─┬─(1)─▷ 0
    ├─(2)─▷ 2
    ├─(1)─▷ 4
    └─(1)─▷ 5

2 ◁─┬─(1)─▷ 0
    ├─(2)─▷ 1
    ├─(1)─▷ 3
    └─(1)─▷ 5

3 ◁─┬─(1)─▷ 2
    └─(1)─▷ 5

4 ◁─┬─(1)─▷ 1
    └─(1)─▷ 5

5 ◁─┬─(1)─▷ 0
    ├─(1)─▷ 1
    ├─(1)─▷ 2
    ├─(1)─▷ 3
    └─(1)─▷ 4
```

If we ever want to reference the neighbors of a specific node, we can do that with the `get_neighbors` function:

```python
for neighbor, weight in my_graph.get_neighbors(5):
    print(f"{neighbor=}, {weight=}")
```
```
neighbor=0, weight=Fraction(1, 1)
neighbor=1, weight=Fraction(1, 1)
neighbor=2, weight=Fraction(1, 1)
neighbor=3, weight=Fraction(1, 1)
neighbor=4, weight=Fraction(1, 1)
```

Finally, graphs have some interesting methods and properties that allow us to analyze them more easily:

The `my_graph.degree(<node number>)` function will give you the degree of a specified node (basically, the sum weight of all edges adjacent to it):

```python
print(my_graph.degree(5))
print(my_graph.degree(2))
```
```
5
5
```

The `my_graph.adjacency_matrix` property allows us to see the adjacency matrix (please see the linear algebra submodule) of the graph:

```python
print(my_graph.adjacency_matrix)
```
```
┌                  ┐
│ 0  1  1  0  0  1 │
│ 1  0  2  0  1  1 │
│ 1  2  0  1  0  1 │
│ 0  0  1  0  0  1 │
│ 0  1  0  0  0  1 │
│ 1  1  1  1  1  0 │ (size: 6×6)
└                  ┘
```

And finally the `my_graph.degree_matrix` property allows us to see the degree matrix of the graph:

```python
print(my_graph.degree_matrix)
```
```
┌                  ┐
│ 3  0  0  0  0  0 │
│ 0  5  0  0  0  0 │
│ 0  0  5  0  0  0 │
│ 0  0  0  2  0  0 │
│ 0  0  0  0  2  0 │
│ 0  0  0  0  0  5 │ (size: 6×6)
└                  ┘
```
