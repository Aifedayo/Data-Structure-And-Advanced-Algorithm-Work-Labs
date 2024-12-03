def binary_sort(arr):
    arr_len = len(arr) - 1
    for i in range(arr_len):
        for j in range(arr_len):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


print(binary_sort([32, 1, 9, 6]))