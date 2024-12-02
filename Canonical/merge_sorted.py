def merge_sorted(arr1, arr2):
    # Use pointers
    left, right = 0,0
    result = []
    
    while left < len(arr1) and right < len(arr2):
        if arr1[left] < arr2[right]:
            result.append(arr1[left])
            left += 1
        else:
            result.append(arr2[right])
            right += 1

    while left < len(arr1):
        result.append(arr1[left])
        left += 1
    while right < len(arr2):
        result.append(arr2[right])
        right += 1

    return result

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted(list1, list2))