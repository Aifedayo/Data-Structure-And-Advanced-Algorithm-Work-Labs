def merge_sorted(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < arr2[j]:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged
        

# Time complexity: 0(n)
# Space complexity: 0(1) Auxilary space