def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [5, 10, 7, 2, 8, 6]
insertion_sort(arr)
print("Sorted array is:", arr)
def binary_search(arr, target):
    """
    Binary search algorithm to find the index of the target value in a sorted array.

    Parameters:
        arr (list): The sorted array to search in.
        target: The value to search for in the array.

    Returns:
        int: Index of the target value in the array if found, otherwise -1.
    """
    # Initialize left and right pointers to the beginning and end of the array
    left = 0
    right = len(arr) - 1

    # Continue searching until the search interval is valid
    while left <= right:
        # Calculate the midpoint of the search interval
        mid = (left + right) // 2

        # Check if the midpoint element is equal to the target
        if arr[mid] == target:
            return mid  # Return the index of the target value

        # If the target is greater than the midpoint, search the right half
        elif arr[mid] < target:
            left = mid + 1

        # If the target is less than the midpoint, search the left half
        else:
            right = mid - 1

    # If the target is not found after the loop, return -1
    return -1


# Example usage
arr = [5, 10, 7, 2, 8, 6]
target = 7
index = binary_search(arr, target)

# Output the result
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the array.")
