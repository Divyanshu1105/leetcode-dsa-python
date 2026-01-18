
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""Traverse Singled linked list using Recursive approach"""
# def recursiveTraverse(current):
#     if current is None:
#         return
#     print(current.data,end="->")
#     recursiveTraverse(current.next)

"""Add the node at the front"""
# def addFront(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     return new_node

"""Add the node at the last"""
# def addLast(head , data):
#     newNode = Node(data)

#     if head is None:
#         return newNode   # first node becomes head

#     curr = head
#     while curr.next:
#         curr = curr.next

#     curr.next = newNode
#     return head

"""Insert the node at a given position"""
# def addAtPosition(head , pos , data):
#     if pos < 1:
#         return head  # invalid position

#     newNode = Node(data)

#     if pos == 1:
#         newNode.next = head
#         return newNode

#     curr = head
#     count = 1

#     while curr and count < pos - 1:
#         curr = curr.next
#         count += 1

#     if curr is None:
#         return head  # position out of bounds

#     newNode.next = curr.next
#     curr.next = newNode
#     return head

def reverseList(head):
    temp = None

    if head.next is None:
        return head
    
    curr = head
    prev = temp

    while curr:
        prev.next = temp
        temp = prev
        prev = curr
        curr = curr.next

    prev.next = temp
    head = prev

    return head

def printList(head):
    curr = head
    while curr:
        print(curr.data,end="->")
        curr = curr.next
    print(None)

def main():
    # head = None    #--> Take head None if no node exists 
    node1 = Node(12)
    node2 = Node(14)
    node3 = Node(16)
    node4 = Node(18)

    node1.next = node2
    node2.next = node3
    node3.next = node4 

    head = node1
    # recursiveTraverse(current)

    
    # head = addFront(head, 10)


    # addLast(head , 20)

    # head = addAtPosition(head, 6, 34)

    head = reverseList(head)
    
    printList(head)

    

if __name__ == "__main__":
    main()
