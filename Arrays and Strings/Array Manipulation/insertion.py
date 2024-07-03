def delete_at_position(arr, position):
    return arr[:position] + arr[position+1:]


arr = [1, 2, 3, 4, 5]
print(delete_at_position(arr, 2))

# Time complexity is O(n): because of slicing 
# Space complexity is O(n): Because we made a new list