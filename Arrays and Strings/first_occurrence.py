def first_occurence(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
            return mid
        elif (nums[mid] == target and nums[mid-1] == target) or nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(first_occurence(nums=[2, 4, 4, 4, 6, 6, 8, 10], target=6))