class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

def printList(head):
    curr = head
    while curr:
        print(curr.val,end="->")
        curr = curr.next
    print(None)


def removeNthFromEnd(head,n):
    if not head:
        return head
    
    curr = head
    length = 0
    #finding lenght of the list
    while curr:
        length += 1
        curr = curr.next

    deleteAt = length
    curr = head
    while curr:
        if n == length:
            curr = curr.next
            head = curr
            return head
        elif deleteAt - 1 == n:
            curr.next = curr.next.next
            return head
        curr = curr.next
        deleteAt -= 1


    return head




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5 

head = removeNthFromEnd(node1,5)
printList(head)