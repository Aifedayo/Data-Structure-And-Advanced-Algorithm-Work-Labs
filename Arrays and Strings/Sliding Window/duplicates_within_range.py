"""
Given an integer array arr and an integer k, 
determine if there are any duplicate values 
within k indices of each other. In other words, 
check if the same value exists at two different 
indices that are at most k positions apart.
"""

def duplicate_in_range(arr, k):
    unique_set = set()

    for right in range(len(arr)):
        if arr[right] in unique_set:
            return True
        unique_set.add(arr[right])
        
    return False

print(duplicate_in_range(arr=[1,2,3,1,4,5],k=3))