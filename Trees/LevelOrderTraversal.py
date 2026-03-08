class Node:
    def __init__(self,val=0 , left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right

def levelOrder(root):
    if root is None:
        return 
    
    q = []
    res = []

    q.append(root)
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            node = q.pop(0)
            res[curr_level].append(node.val)

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        curr_level += 1
    return res

if __name__ == '__main__':

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    # Perform level order traversal and get the result
    res = levelOrder(root)
    for level in res:
        for val in level:
            print(val, end=' ')
        print()