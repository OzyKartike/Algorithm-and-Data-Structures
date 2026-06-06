from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class TestMaxDepth:
    @staticmethod
    def test():
        solution = Solution()

        # Test case 1: Empty tree
        root1 = None
        assert solution.maxDepth(root1) == 0, "Test case 1 failed"

        # Test case 2: Single node tree
        root2 = TreeNode(1)
        assert solution.maxDepth(root2) == 1, "Test case 2 failed"

        # Test case 3: Tree with multiple levels
        #       3
        #      / \
        #     9   20
        #        /  \
        #       15   7
        root3 = TreeNode(3)
        root3.left = TreeNode(9)
        root3.right = TreeNode(20)
        root3.right.left = TreeNode(15)
        root3.right.right = TreeNode(7)
        assert solution.maxDepth(root3) == 3, "Test case 3 failed"

        # Test case 4: Unbalanced tree
        #       1
        #        \
        #         2
        #          \
        #           3
        root4 = TreeNode(1)
        root4.right = TreeNode(2)
        root4.right.right = TreeNode(3)
        assert solution.maxDepth(root4) == 3, "Test case 4 failed"

        print("All test cases passed!")

# Run the tests
TestMaxDepth.test()
