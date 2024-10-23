def is_palindrome_iterative(s):
    s = ''.join(s.split()).lower()

    # pointers
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -=1

    return True


print(is_palindrome_iterative('racescar'))