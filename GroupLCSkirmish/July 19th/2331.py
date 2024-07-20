
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if root.val == 0:
            return False
        if root.val == 1:
            return True
        
        left_val = self.evaluateTree(root.left)
        root_right = self.evaluateTree(root.right)

        if root.val == 2:
            return left_val or root_right
        if root.val == 3:
            return left_val and root_right
        return False
