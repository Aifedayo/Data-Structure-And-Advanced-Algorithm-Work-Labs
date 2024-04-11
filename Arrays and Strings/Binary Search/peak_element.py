"""
A peak element in an array is an element that is greater than its neighbors. 
Given an array nums, find a peak element and return its index. If there are multiple peaks, return the index of any one of the peaks.
"""

def peak_element(nums):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (right + left) // 2

        if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
            return mid
        elif mid > 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1


print(peak_element([1, 2, 1, 3, 5, 6, 4]))