"""
Problem: Given an array of integers, return indices of the two numbers that add up to a 
specific target.
"""

def two_sum(arr, target):
    hashsum = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in hashsum:
            return [hashsum[diff], idx]
        hashsum[num] = idx

    return []
