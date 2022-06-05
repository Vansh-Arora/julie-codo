#Inorder Traversal: Left Root Right

# Recursive InOrder
def inO(root):
    if root == None:
        return
    inO(root.left)
    print(root.data)
    inO(root.right)

# Iterative InOrder
# In inOrder traversal first we reach the left most node

def InO(root):
    stck = []
    ans = []
    first = 1
    curr = root
    while curr or first or len(stck) > 0:
        first = 0
        while curr:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        ans.append(curr.data)
        curr = curr.right

    return ans