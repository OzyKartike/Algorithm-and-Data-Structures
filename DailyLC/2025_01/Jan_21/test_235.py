from sol_235 import Solution, TreeNode

# Helper function to build a binary tree from a list
def build_tree(nodes, index=0):
    if index < len(nodes) and nodes[index] is not None:
        node = TreeNode(nodes[index])
        node.left = build_tree(nodes, 2 * index + 1)
        node.right = build_tree(nodes, 2 * index + 2)
        return node
    return None

# Create a sample binary tree
# Example tree:
#        6
#       / \
#      2   8
#     / \ / \
#    0  4 7  9
#      / \
#     3   5
nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
root = build_tree(nodes)

# Create TreeNode instances for p and q
p = root.left  # TreeNode with value 2
q = root.left.right.right  # TreeNode with value 5

# Create a Solution instance and find the lowest common ancestor
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)

# Print the result
print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val}")