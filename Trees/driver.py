# Structure of a node in a Tree
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

# Function to Build a tree from user input
# Returns root of constructed tree
def build():
    data = int(input())
    if data == -1:
        return None
    nn = Node(data)
    nn.left = build()
    nn.right = build()
    return nn

# Recursive
def preOrder(root):
    if root == None:
        return

    print(root.data)
    preOrder(root.left)
    preOrder(root.right)


root = build()
preOrder(root)