"Problem Statement: Given a list of integers, find the maximum number in the list."

def find_max_elem(lst):
    # Iteratively
    # max_value = lst[0]
    # for num in lst:
    #     if num > max_value:
    #         max_value = num
    # return max_value

    # Recursively

    # base case
    if len(lst) == 1:
        return lst[0]
    max_value = find_max_elem(lst[1:])
    if lst[0] > max_value:
        return lst[0]
    else:
        return max_value
     




arr = [1,10,5,17,2,8,4]
print(find_max_elem(arr))