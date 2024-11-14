def majority_element(arr):
    # freq_map = {}
    # for num in arr:
    #     freq_map[num] = freq_map.get(num, 0) + 1
    
    # for key, count in freq_map.items():
    #     if count > len(arr) // 2:
    #         return key
    # return None


    return max(arr, key=arr.count)
    

arr = [2, 2, 1, 1, 2, 2]
print(majority_element(arr))  # Expected output: 2

arr = [1, 1, 2, 3]
print(majority_element(arr))