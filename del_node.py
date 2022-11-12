def del_node(graph, node):
    """
    (dict, int) -> (dict)
    This function deletes special node from a graph
    >>> del_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, 1)
    {3: [4], 2: [], 4: [3], 5: [2]}
    >>> del_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, "hello")
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if isinstance(node, int) is False:
        return graph
    elif isinstance(graph, dict) is False:
        return None
    elif node in graph:
        del graph[node]
    for value in graph.values():
        if node in value:
            value.remove(node)
    return graph
