def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values to determine bucket ranges
    min_value, max_value = min(arr), max(arr)
    bucket_count = len(arr)  # Number of buckets equal to the array size
    buckets = [[] for _ in range(bucket_count)]  # Creating empty buckets

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1) * (bucket_count - 1))
        buckets[index].append(num)

    # Sort each bucket individually (we can use Insertion Sort, Merge Sort, etc.)
    for i in range(bucket_count):
        buckets[i].sort()

    # Concatenate all buckets into a single sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Example usage:
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print(bucket_sort(arr))
