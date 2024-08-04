class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # Then print the data of node
        print(root.val, end=' ')
        # Now recur on right child
        printInorder(root.right)

def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=' ')
        # Then recur on left child
        printPreorder(root.left)
        # Now recur on right child
        printPreorder(root.right)

def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # Then recur on right child
        printPostorder(root.right)
        # Now print the data of node
        print(root.val, end=' ')

# Construct the binary tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(40)
root.left.right = Node(20)
root.right.left = Node(60)
root.right.right = Node(80)

# Test traversals
print("In-order traversal:")
printInorder(root)

print("\nPre-order traversal:")
printPreorder(root)

print("\nPost-order traversal:")
printPostorder(root)
