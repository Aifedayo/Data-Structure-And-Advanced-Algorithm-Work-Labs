import copy

original_dict = {'name': 'Akeem', 'details': {'age': 30, 'title': 'Engr'}}

shallow_dict_copy = copy.copy(original_dict)

shallow_dict_copy['details']['age'] = 40

print(original_dict)
print(shallow_dict_copy)
