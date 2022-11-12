def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, 6)
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2], 6: []}
    >>> add_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, "lins")
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if isinstance(node, int) is False:
        return graph
    graph[node] = []
    return graph
