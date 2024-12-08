def move_zeros(arr):
    zero_idx = 0
    for idx, n in enumerate(arr):
        if n != 0:
            arr[zero_idx] = n
            if zero_idx  != idx:
                arr[idx] = 0
        zero_idx += 1
    return arr

print(move_zeros)