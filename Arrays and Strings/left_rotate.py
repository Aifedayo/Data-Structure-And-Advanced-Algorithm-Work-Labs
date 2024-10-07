def left_rotate_array(arr, k):
    k = k % len(arr)

    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
print(left_rotate_array(arr, 2))

# Time Complexity: O(n), since you're slicing and concatenating the array.
# Space Complexity: O(n), because a new array is created.
