import string

def cipher(a_string, key):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    encrypt = ''
    for word in a_string:
        if word in lower:
            new = (lower.index(word) + key) % 26
            encrypt += new
        elif word in upper 


print(cipher('word', 3))