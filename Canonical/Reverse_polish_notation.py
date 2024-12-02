def RPN(arr):
    stack = []
    operators = ["+", "*", "-", "/"]
    result = 0
    for val in arr:
        if val not in operators:
            stack.append(val)
        else:
            if val == '+':
                result = float(stack.pop(-2)) + float(stack.pop(-1))
            elif val == '*':
                result = float(stack.pop(-2)) * float(stack.pop(-1))
            elif val == '/':
                result = float(stack.pop(-2)) / float(stack.pop(-1))
            stack.append(str(result))
    return result


arr = ["2", "1", "+", "3", "*"]
arr1 = ["4", "13", "5", "/", "+"]
print(RPN(arr))
    