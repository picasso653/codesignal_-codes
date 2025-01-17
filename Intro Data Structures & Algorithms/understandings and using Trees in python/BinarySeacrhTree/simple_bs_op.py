class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


def minValueNode(node):
    # This function finds the node with the smallest value in a BST
    current = node

    # The smallest value is located at the leftmost leaf.
    # Therefore, we iterate until the left child node is None
    while (current.left is not None):
        current = current.left
    return current

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

def deleteNode(root, key):
    # This function deletes the node containing the value key from the BST

    # If the root is None, then the tree is empty.
    # Therefore, we return the root
    if root is None:
        return root

    # The value key is less than the root's value, then it lies in the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)
    # The value key is greater than the root's value, then it lies in the right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # If the key is equal to the root's key, then this is the node to be deleted

        # If a node with only one child or no child,
        # the root's right child replaces the root if the left child does not exist
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If node has two children, get the inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root

root = Node(6)
insert(root, Node(8))
insert(root, Node(2))
insert(root, Node(5))
insert(root, Node(4))
insert(root, Node(9))
print("In-order traversal:")
in_order_traversal(root)
print("In-order traversal after deleting:")
root = deleteNode(root, 2)
in_order_traversal(root)