def find_first_and_last(arr, target):
    def binary_search_first(arr, target):
        left, right = 0, len(arr)-1
        position = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                position = mid
                right = mid - 1

            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return position
    
    def binary_search_last(arr, target):
        left, right = 0, len(arr)-1
        position = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                position = mid
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return position
    
    first = binary_search_first(arr, target)
    last = binary_search_last(arr, target)
    return [first, last]

arr = [5, 7, 8, 8, 8, 8, 10, 11, 34]
target = 8

print(find_first_and_last(arr, target))