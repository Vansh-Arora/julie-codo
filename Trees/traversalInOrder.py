# Recursive InOrder
def inO(root):
    if root == None:
        return
    inO(root.left)
    print(root.data)
    inO(root.right)

# Iterative InOrder
def InO(root):
    stck = []
    ans = []
    first = 1
    curr = root