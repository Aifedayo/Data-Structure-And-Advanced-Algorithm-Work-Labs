def binary_search(arr, target):
    left, right = 0, len(arr)-1
    position = [-1, -1]

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            if arr[mid-1] == target:
                position[0] = mid-1
                position[1] = mid
            elif arr[mid+1] == target:
                position[0] = mid
                position[-1] = mid+1
            return position
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return position

arr = [5, 7, 7, 7, 8, 8, 10, 11, 34]
target = 8

print(binary_search(arr, target))