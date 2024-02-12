"""
Given an array, write a function to move all the zeros to the end 
while maintaining the relative order of the non-zero elements.
"""
def move_zeros(arr):
    # new_list = ['-inf'] * len(arr)
    # left = 0
    # right = -1
    # for num in arr:
    #     if num > 0:
    #         new_list[left] = num
    #         left += 1
    #     else:
    #         new_list[right] = num
    #         right -=1

    # return new_list
    # Method 2:
    zero_count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[zero_count], arr[i] = arr[i], arr[zero_count]
            print(arr)
            zero_count += 1
    return arr

print(move_zeros([1,2,0,3,4,0,5]))

# Time complexity: O(n)
# Space complexity: O(1)