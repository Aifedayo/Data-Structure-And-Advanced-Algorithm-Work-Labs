class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = Node
            return
        
        curr_head = self.head
        while curr_head.next:
            curr_head = curr_head.next

        curr_head.next = node

    def search(self, data):
        if self.head is None:
            return f'Empty List!'
        
        else:
            curr = self.head
            while curr.next:
                if curr.data == data:
                    return True
                curr = curr.next
        return f'Not found'


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.traverse()  # Expected output: 1 -> 2 -> 3 -> None
ll.delete(2)
ll.traverse()
        

