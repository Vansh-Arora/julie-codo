# Recursive
def preOrder(root):
    if root == None:
        return

    print(root.data)
    preOrder(root.left)
    preOrder(root.right)