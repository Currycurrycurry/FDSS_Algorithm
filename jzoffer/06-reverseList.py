class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printListReversely(node):
    if node:
        printListReversely(node.next)
        print(node.val)

node_list = [Node(i) for i in range(5)]
for i in range(4):
    node_list[i].next = node_list[i+1]
printListReversely(node_list[0])

res = []
def getReverseList(node):
    if node:
        getReverseList(node.next)
        res.append(node.val)
getReverseList(node_list[0])
print(res)

def stackReverse(node):
    stack = []
    while node:
        stack.append(node.val)
        node = node.next
    while stack:
        print(stack.pop())
stackReverse(node_list[0])

        
