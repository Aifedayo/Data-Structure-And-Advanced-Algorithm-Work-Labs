def are_permutations(s1, s2):
    hashmap1 = {}
    hashmap2 = {}

    # Early return
    if len(s1) != len(s2):
        return False
    
    for i in range(len(s1)):
        hashmap1[s1[i]] = hashmap1.get(s1[i], 0) + 1
        hashmap2[s2[i]] = hashmap2.get(s2[i], 0) + 1

    for i in hashmap1:
        if hashmap1[i] != hashmap2.get(i, 0):
            return False
    return True


print(are_permutations("listen", "silent"))  # Expected output: True
print(are_permutations("hello", "world")) 

#Time complexity: O(n), since we are traversing both strings once to build the hashmaps and comparing their frequencies.
# Space complexity: O(n), since we are using two hashmaps to store character frequencies.