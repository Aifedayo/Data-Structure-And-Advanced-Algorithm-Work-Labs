def first_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    return factorial


print(first_factorial(4))