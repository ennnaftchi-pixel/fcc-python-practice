def adjacency_list_to_matrix(adj_list):
    """
    Converts an adjacency list into an adjacency matrix.

    Args:
        adj_list (dict): Dictionary where keys are node indices and
                         values are lists of neighboring node indices.

    Returns:
        list[list[int]]: Adjacency matrix representation of the graph.
    """
    n = len(adj_list)  # number of nodes
    matrix = [[0 for _ in range(n)] for _ in range(n)]  # initialize matrix with 0s

    # Fill edges
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print the adjacency matrix row by row
    for row in matrix:
        print(row)

    return matrix


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1]
    }
    adjacency_list_to_matrix(graph)

"""
I personally like this implementation because 
it is straightforward and easy to understand. 

The use of nested loops to fill the adjacency matrix 
is clear, and printing the matrix row by row helps 
visualize the graph structure. 
Additionally, the function is well-documented, 
making it easy for others to understand its purpose 
and usage.
"""