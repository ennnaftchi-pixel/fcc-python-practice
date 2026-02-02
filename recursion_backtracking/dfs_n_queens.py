def dfs_n_queens(n):
    """
    Solve the N-Queens problem using Depth-First Search (DFS).

    Args:
        n (int): Size of the chessboard (n x n).

    Returns:
        list[list[int]]: A list of solutions, where each solution is a list
        representing queen positions by column index per row.
    """
    if n < 1:
        return []

    solutions = []

    def is_safe(current, col):
        row = len(current)
        for r, c in enumerate(current):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(current):
        if len(current) == n:
            solutions.append(current[:])
            return

        for col in range(n):
            if is_safe(current, col):
                dfs(current + [col])

    dfs([])
    return solutions


if __name__ == "__main__":
    print(dfs_n_queens(4))
