# Recursive
def preOrder(root):
    if root == None:
        return

    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

# Iterative Pre Order
def PreOrder(root):
    stck = []
    ans = []
    curr = root
    while curr or len(stck) > 0:
        while curr:
            ans.append(curr.data)
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        curr = curr.right
    return ans