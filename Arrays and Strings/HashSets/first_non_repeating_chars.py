"""
Given a string, find the first non-repeating character. 
If all characters are repeated, return None.
"""

def first_non_repeating(s):
    seen_once = []
    seen_multiple = set()

    for char in s:
        if char in seen_multiple:
            continue
        if char in seen_once:
            seen_multiple.add(char)
        else:
            seen_once.append(char)
        

    for key, value in hashstring.items():
        if value == 1:
            return key

    return None


print(first_non_repeating('swiss'))
