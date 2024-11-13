import re

def bracket_matcher(brac):
    stack = []
    for bra in brac:
        if bra == '(':
            stack.append(bra)
        elif bra == ')':
            if not stack:
                return False
            stack.pop()
    
    return True if len(stack) == 0 else False
            


print(bracket_matcher('(hello ((world))'))