def del_edge(graph, edge):
    """This function deletes edge from a graph
    >>> del_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, [5,1])
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [2]}
    >>> del_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, 123)

    """
    if isinstance(edge, list) is False:
        return None
    elif isinstance(graph, dict) is False:
        return None
    if edge[0] in graph:
        if edge[1] in graph[edge[0]]:
            graph[edge[0]].remove(edge[1])
    elif edge[1] in graph:
        if edge[0] in graph[edge[1]]:
            graph[edge[1]].remove(edge[0])
    return graph
