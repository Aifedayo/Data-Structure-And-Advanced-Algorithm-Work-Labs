"""
Problem: For a given string, find the length of the longest substring
 without repeating characters
"""

def longest_substring(string):
    right = 0
    max_length = 0
    char_set = set()

    while right < len(string):
        if string[right] in char_set:
            char_set = set()
        char_set.add(string[right])
        right += 1

        max_length = max(max_length, len(char_set))
    return max_length


print(longest_substring('aabbdccc'))