def can_form_palindrome(string):
    freqmap = {}

    for char in string:
        if char in freqmap:
            freqmap[char] -= 1

        else:
            freqmap[char] = 1
    max_count = sum(1 for value in freqmap.values() if value != 0)
    return max_count <= 1



print(can_form_palindrome("civic"))
print(can_form_palindrome("ivicc"))
print(can_form_palindrome("hello")) 
print(can_form_palindrome("aabbh"))