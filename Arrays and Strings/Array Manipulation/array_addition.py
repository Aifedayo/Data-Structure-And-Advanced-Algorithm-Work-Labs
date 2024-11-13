from itertools import combinations

def array_addition(arr):
    max_value = max(arr)
    arr.remove(max_value)
    
    for i in range(1, len(arr)+1):
        for combo in combinations(arr, i):
            if sum(combo) == max_value:
                return True
    return False

print(array_addition([4, 6, 23, 10, 1, 3]))