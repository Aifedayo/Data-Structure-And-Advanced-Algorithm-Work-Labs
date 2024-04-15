def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freqmap = {}

    for i in range(len(s1)):
        freqmap[s1[i]] = freqmap.get(s1[i], 0) + 1
        freqmap[s2[i]] = freqmap.get(s2[i], 0) - 1

    for count in freqmap.values():
        if count >= 1:
            return False
    
    return True


print(anagram('silent', 'lirten'))