def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    This function deletes edge from a graph and return a new graph
    >>> del_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, (5,1))
    {1: [2], 3: [4], 2: [1], 4: [3], 5: [2]}
    >>> del_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, 123)

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if isinstance(edge, tuple) is False:
        return None
    elif isinstance(graph, dict) is False:
        return None
    if edge[0] in graph:
        if edge[1] in graph[edge[0]]:
            graph[edge[0]].remove(edge[1])
    if edge[1] in graph:
        if edge[0] in graph[edge[1]]:
            graph[edge[1]].remove(edge[0])
    return graph
