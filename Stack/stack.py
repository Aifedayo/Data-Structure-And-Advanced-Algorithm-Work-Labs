"""
Task: Implement a Basic Stack
Objective: Create a simple stack data structure using Python. A stack follows the Last In, First Out (LIFO) principle, 
meaning the last element added is the first one to be removed.
"""

# Implement a basic stack :LIFO
class Stack:
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)
        return self.arr
    
    def pop(self):
        try:
            if not self.is_empty():
                return self.arr.pop()
        except Exception as e:
            return str(e)
    
    def peek(self):
        try:
            if not self.is_empty():
                return self.arr[-1]
        except Exception as e:
            return str(e)
    
    def is_empty(self):
        return len(self.arr) == 0 
    
    def size(self):
        return len(self.arr)


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(stack.peek())  # Output: 20
    print(stack.pop()) 
    print(stack.is_empty())
    print(stack.size())
