import unittest
from sol_572 import Solution, TreeNode

class TestIsSubtree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_subtree_true(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)

        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_is_subtree_false(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)

        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        subRoot.right.left = TreeNode(0)

        self.assertFalse(self.solution.isSubtree(root, subRoot))

if __name__ == '__main__':
    unittest.main()