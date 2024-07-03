def find_majority_element(arr):
    # create an hashmap
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    for key, count in freq_map.items():
        if count > len(arr) // 2:
            return key
    return None

