def to_edge_dict(edge_list):
    """This function transforms edge list into a dictionary
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5]])
    {1: [2, 5], 3: [4], 2: [1], 4: [3], 5: [1]}
    
    """
    result_dict = {element[0]: [] for element in edge_list} | {element[1]: [] for element in edge_list}
    for element in edge_list:
        result_dict[element[0]].append(element[1]) 
        result_dict[element[1]].append(element[0]) 
    return result_dict

import doctest
doctest.testmod()