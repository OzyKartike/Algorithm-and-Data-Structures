# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        temparr = [root.val]
        farr = []
        while q:
            print(temparr)
            farr.append(temparr)
            temparr = []
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    temparr.append(node.left.val)
                if node.right:
                    temparr.append(node.right.val)
                    q.append(node.right)
            print(temparr)
        return farr