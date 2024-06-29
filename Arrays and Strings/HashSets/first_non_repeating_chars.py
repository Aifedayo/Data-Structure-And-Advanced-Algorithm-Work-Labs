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

    return seen_once[0] if seen_once else None


print(first_non_repeating('swiss'))
