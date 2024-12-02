def RPN(arr):
    stack = []
    operators = {"+", "*", "-", "/"}
    result = 0
    for val in arr:
        if val not in operators:
            stack.append(float(val))
        else:
            b = stack.pop()
            a = stack.pop()
            if val == '+':
                stack.append(a+b)
            elif val == '-':
                stack.append(a - b)
            elif val == '*':
                stack.append(a * b)
            elif val == '/':
                stack.append(a / b)
    return stack[0]


arr = ["2", "1", "+", "3", "*"]
arr1 = ["4", "13", "5", "/", "+"]
print(RPN(arr))
    