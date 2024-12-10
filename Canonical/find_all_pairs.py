def find_all_pairs(arr, target):
    seen = set()
    result = []
    for num in arr:
        diff = target - num
        if diff in seen:
            result.append((diff, num))
        else:
            seen.add(num)
    return result


print(find_all_pairs([1,2,3,4,5], 5))        
