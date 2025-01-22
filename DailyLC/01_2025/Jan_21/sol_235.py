# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# basic strat check if root.val > low the go right
# if root.val < high then go left
# if root.val is in between low and high then return root.val
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        high = max(p.val, q.val)
        low = min(p.val, q.val)
        if root.val < low:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)
        return root