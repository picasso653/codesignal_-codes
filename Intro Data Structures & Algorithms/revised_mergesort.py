import random
import string

# TODO: Define a merge_sort function that takes data to sort and returns the sorted data
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    lefty = merge_sort(arr[:mid])
    righty = merge_sort(arr[mid:])
    

    return merge(lefty, righty)

# TODO: In the merge function, take two sorted arrays as inputs
def merge(left, right):
    results = []
    i = j = 0
    # TODO: While both arrays have elements in them, compare the first element of each.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

    # TODO: If the left or right array still has elements, add them to the result array.

# TODO: Generate some random data to sort


random_chars = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]

# TODO: Print the original data
print("Original data = ", random_chars)

# TODO: Use your merge_sort function to sort the data
sorted = merge_sort(random_chars)

# TODO: Print the sorted data
print("Sorted = ", sorted)