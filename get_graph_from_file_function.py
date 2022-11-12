def get_graph_from_file(file: str) -> list:
    """This function reads graphs from file and returns a list of graphs
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    graphs = []
    list_graphs = []
    file_content = open(file, "r", encoding = "utf-8")
    graphs = [list(row.strip().split(",")) for row in file_content]
    file_content.close()
    i = 0
    for element in graphs:
        list_graphs.append([])
        for number in element:
            list_graphs[i].append(int(number))
        i+=1
    return list_graphs
