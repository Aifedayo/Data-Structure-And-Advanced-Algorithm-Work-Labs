import copy

def verify_deepcopy():
    
    original_list = [[1,2], [3,4]]
    deep_copy = copy.deepcopy(original_list)

    deep_copy[0][0] = 99

    return original_list, deep_copy

original, copied = verify_deepcopy()
print("Original List:", original)
print("Deep Copied List:", copied)
