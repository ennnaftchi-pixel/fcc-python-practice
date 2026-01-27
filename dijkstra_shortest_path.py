""" 
Dijkstra's Shortest Path Algorithm Implementation
This module implements Dijkstra's algorithm to find the shortest path
"""

INF = float('inf')

# Adjacency matrix representing the weighted graph
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

def shortest_path(matrix, start_node, target_node=None):
    """
    Computes the shortest path(s) from a start node to all other nodes
    or a specific target node using Dijkstra's algorithm.
    """
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        # Find the unvisited node with the smallest distance
        min_distance = INF
        current = -1
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break

        visited[current] = True

        # Update distances to neighbors
        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    # Output results
    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        path = ' -> '.join(str(n) for n in paths[node_no])
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    return distances, paths


if __name__ == "__main__":
    shortest_path(adj_matrix, 0, 5)

