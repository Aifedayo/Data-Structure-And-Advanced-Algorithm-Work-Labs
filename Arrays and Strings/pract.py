from Stack.stack import Stack

def is_balanced(s):
    stack = Stack()

    closing_key = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for brac in s:
        if brac in closing_key:
            if stack.is_empty() or stack.pop() != closing_key[brac]:
                return False
        else:
            stack.push(brac)
    return stack.is_empty()
