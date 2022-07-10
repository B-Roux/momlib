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

Or we could simply look at a single edge, if we wanted to:
```python
print(my_graph.get_edge(0, 1))
print(my_graph.get_edge(1, 2))
print(my_graph.get_edge(4, 0))
```
```
1
2
None
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

## Directed Graphs

Directed graphs work somewhat similarly to "regular" graphs, except in that edges are *directional*, meaning that an edge from node *n* to node *m* is not the same as an edge from node *m* to node *n*. For this reason, you must be careful about being aware of the directionality of any edges you create or reference.

They are created and maintained in much a similar way to undirected graphs:

```python
import momlib.graph as gr

my_directed_graph = gr.DiGraph(5)

my_directed_graph.set_edge(0, 1)
my_directed_graph.set_edge(0, 2)
my_directed_graph.set_edge(1, 2, 2) #Set edge with a weight of 2
my_directed_graph.set_edge(2, 3)
my_directed_graph.set_edge(1, 4)

my_directed_graph.new_node(range(5))

print(my_directed_graph)
```
```
0 □─┬─(1)─▷ 1
    └─(1)─▷ 2

1 □─┬─(2)─▷ 2
    └─(1)─▷ 4

2 □───(1)─▷ 3

5 □─┬─(1)─▷ 0
    ├─(1)─▷ 1
    ├─(1)─▷ 2
    ├─(1)─▷ 3
    └─(1)─▷ 4
```

Though, comparing this directed graph to the undirected one from earlier, you will notice that reverse edges don't exist like they did before.

As such, directed graphs replace the notion of "neighbors" with "parents" and "children." A parent is a node that has an edge from itself to another node, while a child is a node that has an edge from another node to itself. Everywhere where neighbors are mentioned in the undirected graph definition, parents and children are substituted in a directed graph, for example `my_directed_graph.set_parents(...)` or `my_directed_graph.set_children(...)` instead of `my_graph.set_neighbors(...)`.

## Tools

Using the `shortest_paths` function, we can quickly find the shortest path from a given node to every other (reachable) node using Dijkstra's algorithm:

```python
import momlib.graph as gr

my_graph = gr.Graph(5)

my_graph.set_edge(0, 1)
my_graph.set_edge(0, 2)
my_graph.set_edge(1, 2, 2) #Set edge with a weight of 2
my_graph.set_edge(2, 3)
my_graph.set_edge(1, 4)

print(gr.shortest_paths(my_graph, 2))
```
```
(
    [Fraction(1, 1), Fraction(2, 1), Fraction(0, 1), Fraction(1, 1), Fraction(3, 1)], 
    [2, 2, None, 2, 1]
)
```

The first list returned gives us the distance from the source node to the node that corresponds to the index, while the second list returned gives us the parent node of a node that corresponds to the index such that recursively following these nodes leads to the source node (or `None`, if no path exists).

In the example above, finding the path from node 4 (the 5th node) to node 2 (the 3rd node) can be analyzed as follows:

- The distance is given by the first list at index 4, which is `Fraction(3, 1)` or 3.
- The immediate parent of node 4 is given by the second list at index 4, which is node 1. The parent of node 1 is given by the second list at index 1, which is 2. Therefore, the shortest path from node 4 to node 2 is 4 → 1 → 2.

# Quick Tips

The `new_node` function of both graphs returns the index at which the new node was created. You don't ever *need* to keep track of this, but if you wanted to you could use it with dictionaries to give your nodes quick and user-friendly identifiers, such as strings:

