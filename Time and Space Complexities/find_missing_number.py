"""
You are given an array containing n distinct numbers from 0 to n,
but one number is missing. Find the missing number.
"""

def find_missing_number(arr):
    n  = len(arr)
    actual_sum = sum(arr)
    expected_sum = n * (n+1)//2
    return expected_sum - actual_sum


arr = [3,0,2]
print(find_missing_number(arr))

# Time complexity: O(n)
# Space complexity: O(2n)