# Recursive
def preOrder(root):
    if root == None:
        return

    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

# Iterative
def PreOrder(root):
    stck = []
    ans = []
    curr = root
    first = 1
    while curr or first or len(stck) > 0:
        first = 0
        while curr:
            ans.append(curr.data)
            stck.append(curr)
            curr = curr.left
        curr = stck.pop()
        curr = curr.right
    return ans