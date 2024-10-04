class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None values
        self.front = self.rear = -1  # Front and rear pointers
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        # If the queue is empty, set front and rear to 0
        if self.is_empty():
            self.front = 0
        # Increment rear pointer in a circular manner
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        value = self.queue[self.front]
        # If the queue has only one element, reset front and rear pointers
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Increment front pointer in a circular manner
            self.front = (self.front + 1) % self.size
        print(f"Dequeued {value}")
        return value
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue contents:", end=" ")
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size
            print()

if __name__ == "__main__":
    circular = CircularQueue(5)
    circular.enqueue(1)
    circular.enqueue(2)
    circular.enqueue(3)
    print(circular.peek())  # Output: 1
    circular.dequeue()      # Output: Dequeued 1
    print(circular.peek())  # Output: 2
    circular.enqueue(4)
    circular.enqueue(5)
    circular.enqueue(6)
    circular.enqueue(7)     # Queue will be full here
    circular.display()      # Output: 2 3 4 5 6
