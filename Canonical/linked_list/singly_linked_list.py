class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.data))
            node = node.next
        return "->".join(result)

    def append(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return
            
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        return self.__str__()

    def append_list(self, a_list):
        if not a_list:
            return

        if self.head is None:
            self.head = Node(data=a_list[0])
            a_list = a_list[1:]

        current = self.head
        while current.next:
            current = current.next
        
        for data in a_list:
            current.next = Node(data=data)
            current = current.next

        
    def search(self, value):
        if self.head is None:
            return f'Empty list'
        current = self.head
        while current.next:
            if current.data == value:
                return f'Found!'
            current = current.next
        
        return f'Not found'
    
    def delete_node(self, target):
        if self.head and self.head.data == target:
            self.head = self.head.next
            return
        
        curr = self.head
        previous = None
        while curr:
            if curr.data == target:
                previous.next = curr.next
            previous = curr
            curr = curr.next
        
    def reverse(self):
        curr = self.head
        previous = None
        while curr:
            temp = curr.next # preserve the next node before breaking off the link
            curr.next = previous # update the link off the curr topoint to None for astart
            previous = curr
            curr = temp
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while True:
            try:
                slow = self.head.next
                fast = self.head.next.next
                if slow is fast:
                    return True
            except:
                return False


ll = LinkedList()
a_list = list(range(1, 101))
ll.append_list(a_list)
print(ll)
