class Node:
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError('Cannot pop an empty stack!')
        poppedhead = self.head
        self.head = self.head.next
        return poppedhead.data 