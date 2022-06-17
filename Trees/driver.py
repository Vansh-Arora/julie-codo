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


root = build()
print(PostOrder(root))