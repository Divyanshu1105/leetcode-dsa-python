import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def printList(head):
    curr = head
    while curr:
        print(curr.val,end="->")
        curr = curr.next
    print(None)

def mergeKLists(lists):

    heap = []
    counter = 0

    for node in lists:
        if node:
            heapq.heappush(heap,(node.val , counter , node))
            counter += 1

    curr = Node(0)
    dummy = curr

    while heap:
        _,_,smallest = heapq.heappop(heap)
        curr.next = smallest
        curr = curr.next

        if smallest.next:
            heapq.heappush(heap,(smallest.next.val,counter , smallest.next))
            counter += 1

    return dummy.next

        


node1 = Node(1)
node2 = Node(2)
node3 = Node(4)

node1.next = node2
node2.next = node3


node4 = Node(1)
node5 = Node(3)
node6 = Node(10)

node4.next = node5
node5.next = node6

node7 = Node(1)
node8 = Node(3)
node9 = Node(5)

node7.next = node8
node8.next = node9


head = mergeKLists([node1 , node4 , node7])
printList(head)
