"""
Problem: For a given string, find the length of the longest substring
 without repeating characters
"""

def longest_substring(string):
    left = 0
    max_length = 0
    char_set = set()

    for right in range(len(string)):
        while string[right] in char_set:
            char_set.remove(string[left])
            left += 1
            
        char_set.add(string[right])
        
        max_length = max(max_length, right - left + 1)
    return max_length


print(longest_substring('aabbdccc'))