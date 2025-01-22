#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, rootT, subT):
        if not rootT and not subT:
            return True
        if not rootT or not subT or rootT.val != subT.val:
            return False
        return (self.isSameTree(rootT.left, subT.left) and self.isSameTree(rootT.right, subT.right))

# Time complexity: O(N*M)