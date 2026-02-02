from typing import List, Tuple


def binary_search(search_list: List[int], value: int) -> Tuple[List[int], str]:
    """
    Perform binary search on a sorted list.

    Returns:
        - The path of values checked during the search
        - A message indicating whether the value was found
    """
    path_to_target = []
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return path_to_target, "Value not found"


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(binary_search([1, 2, 3, 4, 5, 9], 4))
    print(binary_search([1, 3, 5, 9, 14, 22], 10))

