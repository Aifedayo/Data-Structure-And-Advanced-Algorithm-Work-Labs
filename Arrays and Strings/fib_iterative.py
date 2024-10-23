def fib_iterative(nterm):
    first, second = 0, 1
    value = first + second

    while nterm-1 >= 2:
        temp = value
        value = value + second
        second = temp

        nterm -= 1
    return value

print(fib_iterative(7))
