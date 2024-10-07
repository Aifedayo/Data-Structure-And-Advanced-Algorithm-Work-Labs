"""
Given an array, find the contiguous subarray (containing at least one 
number) which has the largest sum and return its sum.
"""

def maximum_subarray(arr):
    left, curr_sum, max_sum = 0, 0, 0

    while left < len(arr):
        if curr_sum < 0:
            curr_sum = 0
        else:
            curr_sum += arr[left]
            max_sum = max(curr_sum, max_sum)
        left += 1
    return max_sum

arr = [5,4,-1,7,8]
print(maximum_subarray(arr))

# Time complexity: O(n)
# Space complexity: O(1)