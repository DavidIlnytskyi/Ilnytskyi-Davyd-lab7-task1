def add_node(graph, node):
    """This finction adds node to the graph
    >>> add_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, 6)
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2], 6: []}
    >>> add_node({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}, "lins")
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}
    """
    if isinstance(node, int) is False:
        return graph
    graph[node] = []
    return graph
import doctest
doctest.testmod()