class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    tail = dummy# Initialize dummy

    while head1 and head2:
        if head1.data > head2.data:
            tail.next = head1
            head1 = head1.next

        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 else head2

    return dummy.next