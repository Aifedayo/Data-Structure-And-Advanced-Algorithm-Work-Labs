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


print(peak_element([1, 7, 4, 3, 5, 6, 4]))