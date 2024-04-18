"""
Problem: For a given string, find the length of the longest substring
 without repeating characters
"""

def longest_substring(s):
    left = 0 # shrink window
    char_set = set()
    max_length = 0

    for right in range(len(s)):
        while s[right]in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        
        max_length = max(max_length, right - left + 1)

    return max_length
    

print(longest_substring('aabbdccc'))