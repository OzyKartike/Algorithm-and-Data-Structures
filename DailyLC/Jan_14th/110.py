class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        vexbolts = 0
        def depth(newRoot):
            if not newRoot:
                return 0
            
            left = depth(newRoot.left)
            right = depth(newRoot.right)
            if abs(left - right) > 1:
                nonlocal vexbolts
                vexbolts = 1
            return 1 + max(left, right)

        
        depth(root)

        if vexbolts == 1:
            return False
        return True
