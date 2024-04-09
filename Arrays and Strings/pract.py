def first_occurence(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target and (mid == 0 or arr[mid-1] != target):
            return mid
        elif arr[mid] >= target and (mid == 0 or arr[mid-1] == target):
            right = mid - 1
        else:
            left = mid + 1
    return -1
        


print(first_occurence(arr=[2, 4, 4, 4, 6, 6, 8, 10], target=4))