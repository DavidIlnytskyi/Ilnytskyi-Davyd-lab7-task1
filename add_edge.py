def add_edge(graph, edge):
    """This function addes edges to the graph
    >>> add_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, [5,2])
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1, 2]}
    >>> add_edge({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, 123)

    """
    if isinstance(edge, list) is False:
        return None
    if edge[0] in graph:
        graph[edge[0]].append(edge[1])
        return graph
    elif edge [1] in graph:
        graph[edge [1]].append(edge[0])
        return graph
    else:
        return None
import doctest
doctest.testmod()