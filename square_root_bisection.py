def square_root_bisection(number, tolerance=0.01, maximum_iterations=50):
    """
    Approximate the square root of a number using the bisection method.

    Args:
        number (float): Number to compute the square root for.
        tolerance (float): Acceptable error margin.
        maximum_iterations (int): Max iterations before failing.

    Returns:
        float | None: Approximated square root or None if it fails to converge.
    """
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        return number

    low = 0
    high = max(1, number)

    for _ in range(maximum_iterations):
        mid = (low + high) / 2

        if (high - low) <= tolerance:
            return mid

        if mid * mid < number:
            low = mid
        else:
            high = mid

    return None


if __name__ == '__main__':
    result = square_root_bisection(225, 1e-7, 10)
    if result is not None:
        print(f"Square root ≈ {result}")
    else:
        print("Failed to converge")
