from collections import Counter

def anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    
    # return sorted(w1) == sorted(w2)

    ######
    # OR #
    ######
    return Counter(w1) == Counter(w2)

print(anagram('listen', 'silent'))