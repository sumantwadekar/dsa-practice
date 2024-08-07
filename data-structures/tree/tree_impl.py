"""
Tree implementation
"""

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.right = None
        self.left = None


class BSTOperations:

    def insert(self, root, value) -> Node:
        new_node = Node(value)

        # If the tree is empty, treat the new node as root itself
        if not root:
            return new_node

        # If the value is already present in tree, return the node at which it is present
        if root.data == value:
            return root

        # Decide whether to place the new node in the left or right subtree
        # If new value is lesser than root value, find place in the left subtree else right subtree
        if root.data > value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data, sep=' ', end=' ')
        self.inorder(root.right)


bst_obj = BSTOperations()
root = bst_obj.insert(None, 10)
root = bst_obj.insert(root, 20)
root = bst_obj.insert(root, 15)
bst_obj.inorder(root)
root = bst_obj.insert(root, 1)
print()
bst_obj.inorder(root)
print()
