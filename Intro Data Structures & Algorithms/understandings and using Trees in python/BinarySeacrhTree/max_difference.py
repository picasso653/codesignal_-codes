class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def max_height_diff(root):
    max_diff = [0]  # Using list to store max difference as mutable object

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Update max difference if current node's difference is larger
        current_diff = abs(left_height - right_height)
        max_diff[0] = max(max_diff[0], current_diff)

        # Return height of current subtree
        return 1 + max(left_height, right_height)

    if root is None:
        return 0

    # Start the recursive calculation
    height(root)
    return max_diff[0]


# Test samples
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(17)

print(max_height_diff(root))  # Expected output: 1