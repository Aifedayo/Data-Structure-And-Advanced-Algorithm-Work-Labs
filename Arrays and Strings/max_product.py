"""
Given an integer array, find the maximum product of two 
elements such that both elements are different.
"""

def max_product(arr):
    arr.sort()
    return (arr[-1] - 1) * (arr[-2]-1)


arr = [3, 4, 5, 2]
print(max_product(arr))  # Expected output: 12

arr = [1, 5, 4, 5]
print(max_product(arr))  # Expected output: 16

arr = [10, 2, 5, 2]
print(max_product(arr))  # Expected output: 36