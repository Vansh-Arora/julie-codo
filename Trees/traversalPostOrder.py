# Recursive
def postOrer(root):
    if root == None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

# Iterative
def PostOrder(root):
    s1 = [root]
    s2 = []
    ans = []
    while s1:
        curr = s1.pop()
        s2.append(curr)

        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)
    
    while s2:
        curr = s2.pop()
        ans.append(curr.data)
    return ans