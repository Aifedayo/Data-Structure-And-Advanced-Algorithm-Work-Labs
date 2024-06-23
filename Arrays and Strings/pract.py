def longest_two_distinct(s):
    left = 0
    curr_sum = 0
    max_sum = 0

    freqmap = {}
    for right in range(len(s)):
        if s[right] in freqmap:
            freqmap[s[right]] += 1
        else:
            freqmap[s[right]] = 1

        while len(freqmap) > 2:
            freqmap[s[left]] -= 1
            if freqmap[s[left]] == 0:
                del freqmap[s[left]]
            left += 1

        max_sum = max(max_sum, right - left+1)

    return max_sum
            
    

print(longest_two_distinct("eceba"))
