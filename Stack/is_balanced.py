"""
Next Task: Check for Balanced Parentheses
Objective: Write a function that uses a stack to check if a string of 
parentheses is balanced.
"""

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
            if stack.is_empty() or closing_key[brac] != stack.pop():
                return False
        else:
            stack.push(brac)
    return stack.is_empty()

if __name__ == "__main__":
    print(is_balanced("(){}[]"))   # Output: True
    print(is_balanced("([{}])"))   # Output: True
    print(is_balanced("(]"))       # Output: False