class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:  # Handles None or single node
            return False
    
        slow = head
        fast = head
    
        while fast and fast.next:  
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    
        return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2 

# Test the function
solution = Solution()
result = solution.hasCycle(node1)
print(f"Has cycle: {result}")  
