def k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    
    freq_s1 = {}
    freq_s2 = {}

    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1
    for char in s2:
        freq_s2[char] = freq_s2.get(char, 0) + 1

    print(freq_s1)
    print(freq_s2)

    mismatch_count = 0
    for char in freq_s1:
        if char in freq_s2:
            mismatch_count += abs(freq_s1[char] - freq_s2[char])
        else:
            mismatch_count += freq_s1[char]
        print(mismatch_count)

    return mismatch_count // 2 <= k
    # The final division by 2 in the return statement accounts 
    # for each pair of mismatched characters


print(k_anagrams("anagram", "mangaar", 2))
print(k_anagrams("anagram", "grammar", 1))
