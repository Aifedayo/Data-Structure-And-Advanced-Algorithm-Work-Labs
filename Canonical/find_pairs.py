def find_pairs(arr, target):
    sum_of_tar = {}
    for idx, num in enumerate(arr):
        diff = target - num
        if diff in sum_of_tar:
            return [idx, sum_of_tar[diff]]
        else:
            sum_of_tar[num] = idx
    return []


print(find_pairs([1,2,3,4,5,6], 6))