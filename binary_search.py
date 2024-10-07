def binary_search(arr, target):
    left, right = 0, len(arr) - 1 # initialize the pointers
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,3,4,5,6,7]
print(binary_search(arr, 3))

# Time Complexity: O(logn): Run time grows logrithmic since the input size reduces
# Space Complexity: O(1): Space is constant

