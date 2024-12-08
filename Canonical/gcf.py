def gcf(i1, i2):
    if i1 < 0 or i2 < 0:
        raise ValueError('Numbers cannot be negative')
    
    if i1 == 0:
        return i2
    if i2 == 0:
        return i1
    
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    gcf = None

    for i in range(1, smaller+1):
        if i1 % i == 0 and i2 % i == 0:
            gcf = i
    
    return gcf

print(gcf(20, 12))