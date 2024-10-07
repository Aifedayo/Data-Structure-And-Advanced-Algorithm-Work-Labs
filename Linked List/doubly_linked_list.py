"""
Task: Implement a Doubly Linked List
A doubly linked list is similar to a singly linked list but with an additional pointer 
in each node to keep track of the previous node. This allows traversal in both directions 
(forward and backward).
"""

class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next  = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        if self.head:
            self.head.prev = node
        self.head = node



    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return

        # Traverse the list
        curr = self.head
        while curr.next:
            curr = curr.next
        node = Node(data, curr, None)
        curr.next = node

    def delete(self, value):
        if self.head is None:
            print("Empty list")
            return
        
        curr = self.head
        if curr.data == value:
            if curr.next:
                curr.next.prev = None
            self.head = curr.next
            return f"Deleted {value}"
        
        while curr:
            if curr.data == value:
                if curr.next:
                    curr.next.prev = curr.prev
                if curr.prev:
                    curr.prev.next = curr.next
                return f"Deleted {value}"
            curr = curr.next
        return f"{value} not in the list"

    def search(self, key):
        # Implement early return
        if self.head is None:
            return f"{key} not in list"
        
        curr = self.head
        while curr:
            if curr.data == key:
                return (f"{key} is in the list")
            curr = curr.next
        return f"{key} not in the list"
    
    def forward_traverse(self):
        # Implement early return
        if self.head is None:
            return "Empty list, nothing to return"
        
        curr = self.head
        while curr:
            print(curr.data, end="-->" if curr.next else "\n")
            curr = curr.next

    def backward_trasverse(self):
        # Implement early return
        if self.head is None:
            return "Empty list, nothing to return"
        
        curr = self.head
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end="-->" if curr.prev else "\n")
            curr = curr.prev





if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    print(dll.forward_traverse())
    print(dll.backward_trasverse())

    # print(dll.delete(20))  # Output: Deleted 20
    # print(dll.delete(40))
    
    # print(dll.forward_traverse())

    # print(dll.search(20))
    # print(dll.search(40))
