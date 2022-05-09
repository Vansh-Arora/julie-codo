class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def build():
    data = int(input())
    if data == -1:
        return None
    nn = Node(data)
    nn.left = build()
    nn.right = build()
    return nn