def square_root(value):
    left, right = 0, value

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid*mid

        if mid_squared == value:
            return mid
        if mid_squared > value:
            right = mid - 1
        else:
            result = mid
            left = mid + 1
    return result

print(square_root(8))