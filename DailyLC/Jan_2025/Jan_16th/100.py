class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases:
        if not p and not q:  # Both nodes are None
            return True
        if not p or not q:  # One node is None, the other is not
            return False
        if p.val != q.val:  # Node values are different
            return False
        
        # Recurse for left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
