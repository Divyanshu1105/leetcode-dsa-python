class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        """
        The maximum depth is the number of nodes along the longest path from
        the root node down to the farthest leaf node. A leaf node is a node
        with no children. Depth is defined as 0 for an empty tree.
    
        Returns:
            int: The maximum depth of the binary tree.
        
        Time Complexity: O(n), where n is the number of nodes in the tree
        Space Complexity: O(h), where h is the height of the tree (due to recursion stack)
    
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
maxDep = sol.maxDepth(root)
print(maxDep)