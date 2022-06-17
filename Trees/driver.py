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

root = build()
print(PreOrder(root))