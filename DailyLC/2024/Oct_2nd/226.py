from typing import Optional, List

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Function to convert a list to a binary tree
def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None

    def build_tree(index: int) -> Optional[TreeNode]:
        if index >= len(lst) or lst[index] is None:
            return None
        node = TreeNode(lst[index])
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        return node

    return build_tree(0)

# Function to convert a binary tree to a list
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    result = []
    if not root:
        return result

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

def test_invertTree():
    solution = Solution()

    # Test cases
    assert tree_to_list(solution.invertTree(list_to_tree([4, 2, 7, 1, 3, 6, 9]))) == [4, 7, 2, 9, 6, 3, 1]
    assert tree_to_list(solution.invertTree(list_to_tree([2, 1, 3]))) == [2, 3, 1]
    assert tree_to_list(solution.invertTree(list_to_tree([]))) == []

    print("All test cases passed!")

if __name__ == "__main__":
    test_invertTree()


