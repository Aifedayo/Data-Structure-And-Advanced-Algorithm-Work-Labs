def k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    
    freq_s1 = {}
    freq_s2 = {}

    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1
    for char in s2:
        freq_s2[char] = freq_s2.get(char, 0) + 1

    mismatch_count = 0
    for char in freq_s1:
        if char in freq_s2:
            