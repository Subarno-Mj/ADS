

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Convert binary tree into list representation 
def tree_to_list(root):
    result = []

    def add(node, i): # node is the current node, and i its list index
        if node is None:
            return        
         
        # create index for insertion
        while len(result) <= i:
            result.append(None)

        result[i] = node.data
        add(node.left, 2 * i + 1)
        add(node.right, 2 * i + 2)

    add(root, 0)
    return result


# Preorder: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create binary tree
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')


# Display list representation
print("List:", tree_to_list(root))

# Display traversals
print("Preorder:", end=" ")
preorder(root)

print("\nInorder:", end=" ")
inorder(root)

print("\nPostorder:", end=" ")
postorder(root)
