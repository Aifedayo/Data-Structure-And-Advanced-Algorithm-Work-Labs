"""
Given a string, find the first non-repeating character in it. 
Return its index. If it doesn’t exist, return -1.
"""
def repeating(s):
    # Method 1
    # for i in s:
    #     if s.count(i) == 1:
    #         return s.index(i)
    # return -1

    # Method 2
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1


print(repeating('aabbdccc'))

# Time complexity: O(n)
# Space Complexity: 0(n)