"""
Given a string, find the first non-repeating character. 
If all characters are repeated, return None.
"""

def first_non_repeating(s):
    hashstring = {}

    for char in range(len(s)):
        hashstring[s[char]] = hashstring.get(s[char], 0) + 1

    for key, value in hashstring.items():
        if value == 1:
            return key

    return None


print(first_non_repeating('swiss'))
