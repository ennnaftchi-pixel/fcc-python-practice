def merge_sort(array):
    """
    Sorts a list in ascending order using the merge sort algorithm.

    Args:
        array (list): The list to be sorted.

    Returns:
        None: The list is sorted in place.
    """
    if len(array) <= 1:
        return

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:')
    print(numbers)

    merge_sort(numbers)

    print('Sorted array:')
    print(numbers)
