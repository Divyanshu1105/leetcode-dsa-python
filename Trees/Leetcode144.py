class Solution:
    def getList(self, root, output):
        if not root:
            return
        output.append(root.val)
        self.getList(root.left, output)
        self.getList(root.right, output)

    def preorderTraversal(self, root):
        output = []
        self.getList(root, output)
        return output
