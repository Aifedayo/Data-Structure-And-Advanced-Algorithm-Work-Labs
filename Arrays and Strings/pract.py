def delete_at_pos(arr, pos):
    return arr[:pos] + arr[pos+1:]
        

print(delete_at_pos([1,1,2,4,5,5,5,5], 0))