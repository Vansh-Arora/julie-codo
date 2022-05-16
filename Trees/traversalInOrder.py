# Recursive InOrder
def inO(root):
    if root == None:
        return
    inO(root.left)