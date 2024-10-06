def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
 # Time grows quadratically as input size increases

arr = [1,2,3]
print_pairs(arr)