def insertion_sort(arr):
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # Element to be inserted
        j = i - 1  # Index of the previous element
        # Move elements that are greater than the key to the next position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Move the element to the right
            j -= 1
        arr[j + 1] = key  # Place the key in the correct position
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6, 2, 100, 1]
print("Before sorting:", arr)
sorted_arr = insertion_sort(arr)
print("After sorting:", sorted_arr)