"""
Given a string, find the first non-repeating character. 
If all characters are repeated, return None.
"""
def first_non_repeating(string):
    freqmap = {}
    for i in range(len(string)):
        freqmap[string[i]] = freqmap.get(string[i], 0) + 1

    for key, value in freqmap.items():
        if value == 1:
            return key
    return None


print(first_non_repeating('swiss'))