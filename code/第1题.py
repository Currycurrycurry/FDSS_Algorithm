# 1
# 20212226543 黄佳妮

########### input processing ############
# tree_nodes = list(map(int, input().split(' ')))

########### tree definition ############
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

########### core algorithm ############
def maxSplit(root=None):
    sums = []
    def helper(root):
        if root:
            sum_value = helper(root.left) + helper(root.right) + root.val
            sums.append(sum_value)
            return sum_value
        return 0
    
    all_sum = helper(root)
    res = float('-inf')
    for sum_ in sums:
        res = max(res, sum_ * (all_sum - sum_))
    return res

nodes = [Node(i+1) for i in range(6)]
########### test case 1 ############
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
print(maxSplit(root))

nodes = [Node(i+1) for i in range(6)]
########### test case 2 ############
root = nodes[0]
root.right = nodes[1]
nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[3].left = nodes[4]
nodes[3].right = nodes[5]
print(maxSplit(root))

nodes = [Node(i+1) for i in range(6)]
########### test case 3 ############
root = nodes[0]
nodes[0].left = nodes[1]
nodes[1].left = nodes[2]
nodes[2].left = nodes[3]
nodes[3].left = nodes[4]
nodes[4].left = nodes[5]
print(maxSplit(root))

nodes = [Node(i+1) for i in range(6)]
########### test case 4 ############
root = nodes[0]
nodes[0].right = nodes[1]
nodes[1].right = nodes[2]
nodes[2].right  = nodes[3]
nodes[3].right  = nodes[4]
nodes[4].right  = nodes[5]
print(maxSplit(root))

########### test case 5 ############
print(maxSplit(None))

########### test case 6 ############
print(maxSplit(Node(0)))

########### test case 7 ############
print(maxSplit())

########### test case 8 ############
nodes = [Node(i+1) for i in range(7)]
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
print(maxSplit(root))

########### test case 9 ############
nodes = [Node(1) for i in range(7)]
root = nodes[0]
root.left = nodes[1]
root.right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]
nodes[2].right = nodes[6]
print(maxSplit(root))