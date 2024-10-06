def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Time complexity is O(n) Becuase we will have to check through the all list
# Space Complexity is O(1) Because we are swapping the item in max_val