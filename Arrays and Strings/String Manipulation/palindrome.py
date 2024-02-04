def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("racecar"))  # Expected output: True
print(is_palindrome("hello")) 

# Time Complexity: O(n), where n is the length of the string. This is because reversing the string takes linear time, and the comparison between the original and reversed string also takes linear time.
# Space Complexity: O(n), since a new string (the reversed version) is created in memory.