

# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insertion
def insert(root, data):   # root = parent node
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Find minimum value in right sub-tree (in-order Successor)
def find_min(root):
    while root.left is not None:
        root = root.left
    return root


# Deletion
def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:   # match found 

        # Case 1: Leaf node
        if root.left is None and root.right is None:
            return None

        # Case 2: Node has only right child
        elif root.left is None:
            return root.right

        # Case 2: Node has only left child
        elif root.right is None:
            return root.left

        # Case 3: Node has two children
        temp = find_min(root.right)  # find & replace with in-order successor
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Inorder traversal ( sorted )
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Create BST
root = None

for value in [50, 30, 70, 20, 40, 60, 80, 65]:
    root = insert(root, value)

print("Original BST:")
inorder(root)

# Delete a leaf node
root = delete(root, 20)
print("\nAfter deleting leaf node 20:")
inorder(root)

# Delete a non-leaf node with one child
root = delete(root, 60)
print("\nAfter deleting node 60 (one child):")
inorder(root)

# Delete a non-leaf node with two children
root = delete(root, 70)
print("\nAfter deleting node 70 (two children):")
inorder(root)

print()
