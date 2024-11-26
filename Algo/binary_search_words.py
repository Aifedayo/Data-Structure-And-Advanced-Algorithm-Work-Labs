def binary_search_words(words, target):
    left, right = 0, len(words)-1

    while left <= right:
        mid = (right + left) // 2
        if words[mid] == target:
            return mid
        elif words[mid][0] > target[0]:
            right = mid - 1
        else:
            left = mid + 1

    return False


print(binary_search_words(['apple', 'banana', 'carrot', 'date', 'egg'], 'apple'))