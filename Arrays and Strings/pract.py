def smallest_subar(arr, k):
    curr_sum = 0
    max_sum = 0

    for i in range(k):
        curr_sum += arr[i]

    max_sum = curr_sum

    for i in range(k, len(arr)):
        curr_sum = curr_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(smallest_subar(arr=[2,1,5,1,3,2], k=3))
