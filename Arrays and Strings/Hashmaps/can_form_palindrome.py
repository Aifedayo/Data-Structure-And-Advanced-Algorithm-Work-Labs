def can_form_palindrome(s):
    
    # uSe hashmap
    freqmap = {}

    for char in s:
        freqmap[char] = freqmap.get(char, 0) + 1
    
    odd_count = sum(1 for count in freqmap.values() if count % 2 != 0)
        
    return odd_count <= 1





print(can_form_palindrome("civic"))
print(can_form_palindrome("ivicc"))
print(can_form_palindrome("hello")) 
print(can_form_palindrome("aabbh"))