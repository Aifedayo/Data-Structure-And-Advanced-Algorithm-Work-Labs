def max_sum_subarray(arr, key):
    max_sum = 0
    window_sum = 0

    for i in range(key):
        window_sum += i

    max_sum = window_sum

    for i in range(key, len(arr)):
        window_sum = window_sum - arr[i - key] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Test case
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))