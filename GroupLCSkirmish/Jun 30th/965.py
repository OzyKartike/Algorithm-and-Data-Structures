class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #DFS
        if not root:
            return True
        if root.left:
            if root.val != root.left.val:
                return False
        if root.right:
            if root.val != root.right.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
