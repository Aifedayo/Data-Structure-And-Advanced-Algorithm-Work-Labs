def fib_iterative(nterm):
    if nterm == 0:
        return 0
    
    elif nterm == 1:
        return 1
    
    first, second = 0, 1

    for _ in range(2, nterm+1):
        first, second = second, first + second
    
    return second

print(fib_iterative(7))
