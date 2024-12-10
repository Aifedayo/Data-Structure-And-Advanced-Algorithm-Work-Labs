import copy

original_list = [[1,2], [3,4]]
shallow_copy = copy.copy(original_list)

shallow_copy[0][0] = 90

print(shallow_copy)
print(original_list)