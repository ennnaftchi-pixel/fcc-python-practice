def dfs(matrix, start_node):
    """
    Perform Depth-First Search (DFS) on a graph represented as an adjacency matrix.

    Args:
        matrix (list[list[int]]): Adjacency matrix of the graph.
        start_node (int): Index of the starting node.

    Returns:
        list[int]: Order of nodes visited during DFS.
    """
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            result.append(current)

            for neighbor in range(len(matrix) - 1, -1, -1):
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return result


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    print(dfs(graph, 0))
