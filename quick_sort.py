def quick_sort(integer_list):
    """
    Sorts a list of integers using the quick sort algorithm.

    This implementation is not in-place and returns a new sorted list.

    Args:
        integer_list (list): List of integers to sort.

    Returns:
        list: A new sorted list.
    """
    if len(integer_list) <= 1:
        return integer_list.copy()

    pivot = integer_list[0]

    lesser = [x for x in integer_list if x < pivot]
    equal = [x for x in integer_list if x == pivot]
    greater = [x for x in integer_list if x > pivot]

    return quick_sort(lesser) + equal + quick_sort(greater)


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted list:')
    print(numbers)

    sorted_numbers = quick_sort(numbers)

    print('Sorted list:')
    print(sorted_numbers)
