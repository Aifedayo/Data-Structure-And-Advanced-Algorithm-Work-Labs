"""
Task: Implement a Basic Stack
Objective: Create a simple stack data structure using Python. A stack follows the Last In, First Out (LIFO) principle, 
meaning the last element added is the first one to be removed.
"""

# Implement a basic stack :LIFO
class Stack:
    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self, item):
        self.arr.append(item)
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        return self.arr
    
    def pop(self):
        if not self.is_empty():
            item = self.arr.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()
        return item
    
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
    
    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None



if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(2)
    stack.push(20)
    stack.push(5)
    stack.push(15)
    stack.push(4)
    # print(stack.peek())  # Output: 20
    # print(stack.pop()) 
    print(stack.get_min())
    print(stack.is_empty())
    print(stack.size())
