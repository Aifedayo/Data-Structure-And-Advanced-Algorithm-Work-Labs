"""
Write a function that takes two lists of integers, list1 and list2, 
and returns a list containing the unique elements that appear in 
both list1 and list2. Each element in the result should appear only 
once, regardless of how many times it appears in each list.
"""

def find_intersection(arr1, arr2):
    # using hash sets can be very effective for this 
    # problem since sets ony store unique values
    hash_set = set()