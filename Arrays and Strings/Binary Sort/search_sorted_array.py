"""
Given a sorted array nums that has been rotated at an unknown pivot, 
write a function to search for a target value in this array. 
If the target exists, return its index; otherwise, return -1.
"""

def search_rotated(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (right + left ) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= nums[mid] and target <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1 
            return mid
    return -1

print(search_rotated(nums=[4,5,6,7,0,1,2], target=3))
            