def find_majority_element(arr):

    return max(set(arr), key=arr.count)
        

print(find_majority_element([1,1,2,4,5,5,5,5]))