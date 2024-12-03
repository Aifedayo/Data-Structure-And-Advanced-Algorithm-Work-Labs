def fib_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    table = [0] * (n+1)
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(fib_dp(10))

def binary_sort(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left+ right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1