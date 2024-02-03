"""
Write a function that takes two lists of integers, list1 and list2, 
and returns a list containing the unique elements that appear in 
both list1 and list2. Each element in the result should appear only 
once, regardless of how many times it appears in each list.
"""

def find_intersection(arr1, arr2):
    # using hash sets can be very effective for this 
    # problem since sets ony store unique values
    
    unique_set = set()
    i = 0
    if len(arr1) > len(arr2):
        while i < len(arr1):
            if arr1[i] in arr2:
                unique_set.add(arr1[i])
            i += 1
    else:
        while i < len(arr2):
            if arr2[i] in arr1:
                unique_set.add(arr2[i])
            i += 1

    return list(unique_set)

    ###############################################
    #            SIMPLIFIED SOLUTION              #
    #   set1 = set(arr1)                          #
    #   set2 = set(arr2)                          #
    #   # Find the intersection of both sets      #
    #   return list(set1 & set2)                  #
    ###############################################
list1 = [4, 9, 5]
list2 = [9, 4, 9, 8, 4]

print(find_intersection(list1, list2))
            
