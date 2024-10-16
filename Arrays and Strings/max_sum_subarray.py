def max_sum_subarray(arr, k):
    left = 0
    right = k
    max_sum = 0

    while right < len(arr)+1:
        max_sum = max(max_sum, sum(arr[left:right]))
        left += 1
        right += 1

    return max_sum

print(max_sum_subarray(arr=[1,3,5,6], k=3))