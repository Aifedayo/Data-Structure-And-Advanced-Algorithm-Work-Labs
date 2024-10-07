"""
Given an array of integers and a target value, write a function to 
find two numbers in the array that add up to the target value.
"""

def two_sum(arr, target):
    hashsum = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in hashsum:
            return [hashsum[diff], idx]
        else:
            hashsum[num] = idx
    return []

arr = [3,2,4]
target = 6

print(two_sum(arr, target))

# Time complexity: O(n)
# Space complexity: O(n)
