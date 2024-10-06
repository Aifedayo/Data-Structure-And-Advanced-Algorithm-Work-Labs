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




if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
