def find_first_and_last(arr, target):
    def first(arr, target):
        left, right = 0, len(arr)-1
        position = -1

        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                position = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return position
    
    def last(arr, target):
        left, right = 0, len(arr)-1
        position = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                position = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return position
    
    first = first(arr, target)
    last = last(arr, target)
    return [first, last]
        

arr = [5, 7, 8, 8, 8, 8, 10, 11, 34]
target = 11

print(find_first_and_last(arr, target))