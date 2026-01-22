class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    curr = head
    while curr:
        print(curr.data,end="->")
        curr = curr.next
    print(None)

def mergeTwoList(head1, head2):
    dummy = Node(0)
    curr = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next 
        curr = curr.next

    curr.next = head1 or head2
    return dummy.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(4)

node1.next = node2
node2.next = node3


node4 = Node(1)
node5 = Node(3)
node6 = Node(4)

node4.next = node5
node5.next = node6

res = mergeTwoList(node1 , node4)
printList(res)

