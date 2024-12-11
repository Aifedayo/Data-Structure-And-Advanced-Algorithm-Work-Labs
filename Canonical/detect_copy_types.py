import copy

def detect_copy_types(obj1, obj2):
    if obj1 == obj2:
        if all(id(a) == id(b) for a,b in zip(obj1, obj2)):
            return 'shallow Copy'
        else:
            return 'Deep copy'
    return 'unrelated objects'

original_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

print(detect_copy_types(original_list, shallow_copy))
print(detect_copy_types(original_list, deep_copy))