def square_root(x):
    if x < 2:
        return x
    
    left, right = 0, x

    while left <= right:
        mid = (right + left)//2
        print('mid: ', mid)
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        
        elif mid_squared < x:
            left = mid + 1
            result = mid # Saving potential value
        else:
            right = mid - 1

    return result

print(square_root(8))