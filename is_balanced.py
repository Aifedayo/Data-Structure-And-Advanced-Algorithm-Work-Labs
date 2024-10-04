from stack import Stack

def is_balanced(s):
    stack = Stack()
    closing_key = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for brac in s:
        if brac in closing_key:
            if stack.is_empty():
                return False
            else:
                if closing_key[brac] == stack.peek():
                    stack.pop()
                else:
                    return False
        else:
            stack.push(brac)
    return True

if __name__ == "__main__":
    print(is_balanced("(){}[]"))   # Output: True
    print(is_balanced("([{}])"))   # Output: True
    print(is_balanced("(]"))       # Output: False