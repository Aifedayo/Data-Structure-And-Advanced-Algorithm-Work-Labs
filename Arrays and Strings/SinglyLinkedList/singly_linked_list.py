"""
Task: Implement a Linked List
A linked list is a linear data structure where elements are stored in nodes, 
and each node points to the next one. Unlike arrays, linked lists don't store 
data in contiguous memory locations.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value, self.head) # Create a new node with the given data
        self.head = node # head now points to the new node


    def insert_at_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            
            current.next = node
        
    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if curr is None:
            print("None with value", key, "not found")
        
        prev.next = curr.next

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def traverse(self):
        if self.head is None:
            print('Linked list is empty')
            return
        curr = self.head
        while curr:
            print(curr.data, end=" " if curr.next else "\n")
            curr = curr.next


    """
    Concept: Detecting a Cycle in a Linked List
    A cycle (or loop) in a linked list occurs when a node points 
    back to one of the previous nodes, creating an endless loop. 
    Detecting this is important because a cycle can cause infinite 
    loops in traversals, leading to performance issues or even system crashes.
    """
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    ll.traverse()  # Output: 20 -> 10 -> 40 -> 50

    ll.delete_node(20)
    ll.traverse()  # Output: 10 -> 40 -> 50

    print(ll.search(40))  # Output: True
    print(ll.search(99))  # Output: False
