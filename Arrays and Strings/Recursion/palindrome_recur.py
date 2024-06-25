def is_palindrome(s):
    s = ''.join(s.split()).lower()
    if len(s) <= 1:
        return True
    
    
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
    

print(is_palindrome('racsecar'))
