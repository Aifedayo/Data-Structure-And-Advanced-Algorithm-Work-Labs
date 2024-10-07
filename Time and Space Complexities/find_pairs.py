def find_pairs(arr, target):
    seen = []
    pairs = []
    for num in arr: # 1,3,2,4 --> target 5
        diff = target - num # 5 - 4 = 1
        if diff in seen:
            pairs.append((num, diff))
        else:
            seen.append(num) # 1, 3
    return pairs


print(find_pairs([1,3,4,2], target=5))

# Time complexity: O(n)
# Space complexity: O(2n)