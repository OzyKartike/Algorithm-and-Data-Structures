class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0

        def sumOfAll(node):
            if not node:
                return 0
            sumX = sumOfAll(node.left) + sumOfAll(node.right)
            return node.val + sumX
        def totalTilt(node):
            if not node:
                return 0
            x = abs(sumOfAll(node.left) - sumOfAll(node.right))
            tiltLeft = totalTilt(node.left)
            tiltRight = totalTilt(node.right)
            return tiltLeft + x + tiltRight
        x = totalTilt(root)
        return x
