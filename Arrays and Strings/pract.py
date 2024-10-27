class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
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
            return 'Empty List!'
        
        else:
            curr = self.head
            while curr:
                if curr.data == data:
                    return True
                curr = curr.next
        return False
    
    def delete(self, data):
        if self.head is None:
            return 'Empty List'
        
        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next
        return 'Value not found'
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev
    
    def delete_node(self, key):
        curr = self.head
        prev = None

        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return


            


ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.traverse()  # Expected output: 1 -> 2 -> 3 -> None
ll.delete(2)
ll.traverse()
        

