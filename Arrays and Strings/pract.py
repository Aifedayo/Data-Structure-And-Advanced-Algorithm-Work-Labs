def peak_element(arr):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1] and mid > 0:
            return mid
        if arr[mid] < arr[mid-1] and mid > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1 
        

print(peak_element([1, 2, 1, 3, 5, 6, 4]))