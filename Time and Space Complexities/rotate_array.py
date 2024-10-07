def rotate_array(arr,k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


arr = [1,2,3,4,5]
k = 4
print(rotate_array(arr, k))

# Time complexity: O(n)
# Space complexity: O(n)