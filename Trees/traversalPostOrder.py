# Recursive
def postOrer(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

# Iterative
def PostOrder(root):
    stck = []
    ans = []
    curr = root
    while curr or len(stck) > 0:
        while curr:
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        