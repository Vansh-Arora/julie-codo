#Inorder Traversal: Left Root Right

# Recursive InOrder
def inO(root):
    if root == None:
        return
    inO(root.left)
    print(root.data)
    inO(root.right)

# Iterative InOrder
## In inOrder traversal first we reach the left most node
## and keep these in a stack, then pop elements and print them and move to right
def InO(root):
    stck = []
    ans = []
    curr = root
    while curr or len(stck) > 0:
        while curr:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        ans.append(curr.data)
        curr = curr.right

    return ans