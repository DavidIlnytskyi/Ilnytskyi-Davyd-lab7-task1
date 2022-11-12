def add_edge(graph, edge):
    """
    (dict, tuple) -> dict
    This function addes edges to the graph
    >>> add_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, (5, 2))
    {1: [2, 5], 3: [4], 2: [1, 5], 4: [3], 5: [1, 2]}
    >>> add_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, 123)

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if isinstance(edge, tuple) is False:
        return None
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
    if edge[1] in graph:
        graph[edge [1]].append(edge[0])
    return graph
