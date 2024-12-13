def check_parentheses(a_string):
    stack = []
    for par in a_string:
        if par == '(':
            stack.append(par)
        elif par == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0