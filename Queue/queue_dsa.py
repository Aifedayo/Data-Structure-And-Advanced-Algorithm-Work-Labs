"""
Task: Implement a Basic Queue
Objective: Create a simple queue data structure using Python. A queue follows the First In, First Out (FIFO) principle, 
meaning the first element added is the first one to be removed.
"""

# Implement a Queue : FIFO
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        return self.queue.appendleft(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())  # Output: 1
    print(queue.dequeue())  # Output: 1
    print(queue.is_empty())  # Output: False
    print(queue.size())  # Output: 2
