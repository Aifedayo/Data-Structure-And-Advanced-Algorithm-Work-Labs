def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    # using hashmap
    freqmap1 = {}
    freqmap2 = {}

    for i in range(len(s1)):
        freqmap1[s1[i]] = freqmap1.get(s1[i], 0) + 1
        freqmap2[s2[i]] = freqmap2.get(s2[i], 0) + 1

    for i in freqmap1:
        if freqmap1[i] != freqmap2.get(i, 0):
            return False
    
    return True
    

print(anagram('silent', 'listen'))
