def is_edge_in_graph(graph, edge):
    """This function checks if edge is in graph
    >>> is_edge_in_graph({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, [2,5])
    False
    >>> is_edge_in_graph({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, [1,5])
    True
    >>> is_edge_in_graph({1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}, 123)

    """
    if isinstance(edge, list) == False:
        return None
    if isinstance(graph, dict) == False:
        return None

    if edge[1] > len(graph):
        return None
    if edge[0] > len(graph):    
        return None
    if edge[1] in graph[edge[0]]:
        return True
    elif edge[0] in graph[edge[1]]:
        return True
    else:
        return False
import doctest
doctest.testmod()