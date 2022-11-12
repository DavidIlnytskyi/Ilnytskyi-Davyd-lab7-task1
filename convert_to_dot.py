def convert_to_dot(graph):
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    >>> convert_to_dot(123)

    """
    if isinstance(graph, dict) is False:
        return None
    connections = []
    for element in graph.items():
        for value in element[1]:
            connections.append(f"{element[0]} -- {value}")
    dot_file = open ("graph.dot", "w", encoding = "utf-8")
    dot_file.write("graph {\n")
    for connect in connections:
        dot_file.write(connect + "\n")
    dot_file.write("}")
    dot_file.close()
