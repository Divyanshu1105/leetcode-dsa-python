class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    """
    Builds a binary tree from preorder and inorder traversal lists.

    Args:
        preorder: List of values, root always comes first.
        inorder:  List of values, root always sits in the middle.

    Returns:
        Root TreeNode of the constructed tree.
    """
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val) #use O(n) time because it scans full list 
                                 # instead of index() we can use Hashamp for O(1) work. 

    root.left = buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildTree(preorder[mid+1:],inorder[mid+1:])

    return root

def printTree(root):
    if root is None:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

preorder = [1,2,4,5,3,6,7]
inorder = [4,2,5,1,6,3,7]
root = buildTree(preorder , inorder)
printTree(root)