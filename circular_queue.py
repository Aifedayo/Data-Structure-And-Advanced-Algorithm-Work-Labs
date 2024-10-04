"""
Next Task: Implement a Circular Queue
In a circular queue, the last position is connected back to the first position 
to form a circle. This type of queue is useful in applications like traffic 
light cycles or buffering.
"""
from collections import deque

class CircularQueue:
    def __init__(self):
        self.circular_queue = deque()

    def is_empty(self):
        return len(self.circular_queue) == 0
    
    def size(self):
        return len(self.circular_queue)
    
    def enqueue(self, item):
        return self.circular_queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            value = self.circular_queue.pop()
            self.enqueue(value)
            return value
    
    def peek(self):
        if self.is_empty():
            return 'Empty Queue'
        return self.circular_queue[-1]
    

if __name__ == "__main__":
    circular = CircularQueue()
    circular.enqueue(1)
    circular.enqueue(2)
    circular.enqueue(3)
    print(circular.peek())
    print(circular.dequeue())
    print(circular.peek())
    print(circular.is_empty())
    print(circular.size())