# TODO: Define your Node class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# TODO: Define a binary tree using your Node class
tree_node = TreeNode('1')
tree_node.left = TreeNode('2')
tree_node.right = TreeNode('3')
tree_node.left.left = TreeNode('4')
tree_node.left.right = TreeNode('5')
tree_node.right.right = TreeNode('6')


# TODO: Implement a function to perform in-order traversal
def inorder(node):
    if node is None:
        return
    else:
        inorder(node.left)
        print(f'{node.value} -> ', end=" ")
        inorder(node.right)


# TODO: Print the nodes of the binary tree using the in-order traversal method
inorder(tree_node)