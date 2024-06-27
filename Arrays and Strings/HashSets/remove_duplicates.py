def remove_duplicates(nums):
    unique_nums = set()
    result = []

    for num in nums:
        if num in unique_nums:
            pass
        else:
            unique_nums.add(num)
    
    return list(unique_nums)


print(remove_duplicates([1,1,2,3,4,5,5]))