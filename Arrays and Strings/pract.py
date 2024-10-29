"""
Given a string s, find the length of the longest substring 
that contains at most two distinct characters.
"""

def longest_two_distinct(s):
    freqmap = {}
    left = 0
    max_count = 0

    for right in range(len(s)):
        freqmap[s[right]] = freqmap.get(s[right], 0) + 1
        
        while len(freqmap) > 2:
            freqmap[s[left]] -= 1
            if freqmap[s[left]] == 0:
                del freqmap[s[left]]
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count

            

print(longest_two_distinct("eceeeeba"))