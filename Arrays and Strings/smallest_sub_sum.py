def smallest_sub_array(arr, S):
    window_sum = 0
    min_length = float('inf')
    left = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= S:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0


print(smallest_sub_array(arr=[2,1,5,2,3,2], S=7))