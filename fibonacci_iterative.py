def fibonacci(n):
    """
    Compute the nth Fibonacci number using an iterative approach.

    Args:
        n (int): The index of the Fibonacci number (n >= 0).

    Returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n < 2:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(10))
