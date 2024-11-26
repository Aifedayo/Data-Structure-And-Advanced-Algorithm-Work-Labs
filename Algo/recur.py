def print_num(n):
    # base case
    if n == 1:
        return 1
    print(n)
    return print_num(n-1)

print(print_num(10))