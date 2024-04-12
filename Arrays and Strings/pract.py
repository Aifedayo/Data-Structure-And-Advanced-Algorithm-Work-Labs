def search_rotated(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target <= nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target <= nums[mid] and target <= nums[left]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

print(search_rotated(nums=[4,5,6,7,0,1,2], target=2))