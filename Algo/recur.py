def print_num(n):
    # base case
    if n > 10:
        return
    print(n)
    return print_num(n+1)

print(print_num(1))