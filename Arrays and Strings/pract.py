"""
Given a string, find the first non-repeating character in it. 
Return its index. If it doesn’t exist, return -1.
"""

def repeating(s):
    # using hashset
    seen_once = []
    seen_multiple = set()
    for char in s:
        if char not in seen_once:
            seen_once.append(char)
        else:
            seen_once.remove(char)
            seen_multiple.add(char)
    return seen_once[0] if seen_once else None\
    

print(repeating('swiss'))