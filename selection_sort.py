def selection_sort(items):
    """
    Sort a list of items in ascending order using the selection sort algorithm.
    
    Args:
        items (list): The list of comparable elements to sort.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Example:
        >>> selection_sort([4, 2, 5, 1])
        [1, 2, 4, 5]
    """
    n = len(items)
    
    for i in range(n - 1):  # iterate through each position
        min_index = i
        
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
    
    return items

if __name__ == '__main__':
    numbers = [64, 25, 12, 22, 11]
    print("Original list:", numbers)
    sorted_numbers = selection_sort(numbers)
    print("Sorted list:  ", sorted_numbers)

