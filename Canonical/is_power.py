def is_power(n):
    if n & (n-1) == 0:
        return True
    
    return False

print(is_power(16))