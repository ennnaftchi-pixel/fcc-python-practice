def gen_parentheses(pairs):
    """
    Generate all valid combinations of parentheses for a given number of pairs.

    Args:
        pairs (int): Number of parentheses pairs.

    Returns:
        list[str]: All valid parentheses combinations.
    """
    if not isinstance(pairs, int):
        raise TypeError("The number of pairs must be an integer")
    if pairs < 1:
        raise ValueError("The number of pairs must be at least 1")

    queue = [("", 0, 0)]  # (current_string, opens_used, closes_used)
    result = []

    while queue:
        current, opens_used, closes_used = queue.pop(0)

        if len(current) == 2 * pairs:
            result.append(current)
            continue

        if opens_used < pairs:
            queue.append((current + "(", opens_used + 1, closes_used))

        if closes_used < opens_used:
            queue.append((current + ")", opens_used, closes_used + 1))

    return result


if __name__ == "__main__":
    print(gen_parentheses(2))
    print(gen_parentheses(3))
