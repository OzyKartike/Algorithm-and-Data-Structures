# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []  
        def f(root, l):
            if not root:
                return
            if l == len(res):
                res.append(root.val) 
            f(root.right, l + 1)  
            f(root.left, l + 1)  
        f(root, 0)  
        return res
