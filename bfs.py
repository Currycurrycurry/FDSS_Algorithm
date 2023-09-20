# TODO 二叉树的最小深度
# visited 的主要作用是防止走回头路，大部分时候都是必须的，但是像一般的二叉树结构，没有子节点到父节点的指针，不会走回头路就不需要 visited。

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def levelorder(root):
    if not root:
        return []
    heap = [root]
    ans = []
    while len(heap) != 0:
        node = heap.pop(0)
        ans.append(node.val)
        if node.left:
            heap.append(node.left)
        if node.right:
            heap.append(node.right)
    return ans

    
def minDepth(root):
    if not root:
        return 0
    heap = [root]
    depth = 1
    while len(heap) != 0:
        for i in range(len(heap)):
            node = heap.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                heap.append(node.left)
            if node.right:
                heap.append(node.right)
        depth += 1
    return depth

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4

print(minDepth(root))
print(levelorder(root))
        

# 打开转盘锁
# 752. 打开转盘锁 就是在有dead锁条件的情况下 用BFS算密码算扭动的最少次数
def addOne(num, i):
    return num[:i] + str(int(num[i]) + 1)[-1] + num[i+1:]

def subOne(num, i):
    tmp = '9' if num[i] == '0' else str(int(num[i]) - 1)
    return num[:i] + tmp + num[i+1:]

def openLock(self, deadends: List[str], target: str) -> int:
    if target == '0000':
        return 0
    heap = ['0000']
    visited = ['0000']
    step = 0
    while len(heap) != 0:
        for i in range(len(heap)):
            node = heap.pop(0)  
            if node == target:
                return step
            if node in deadends:
                return -1
            # 如果你只转一下锁，有几种可能？总共有 4 个位置，每个位置可以向上转，也可以向下转，也就是有 8 种可能对吧。
            for j in range(4):
                add_ans = addOne(node, j)
                if add_ans not in deadends and add_ans not in visited:
                    visited.append(add_ans)
                    heap.append(add_ans)
                sub_ans = subOne(node, j)
                if sub_ans not in deadends and sub_ans not in visited:
                    visited.append(sub_ans)
                    heap.append(sub_ans)
        step += 1
    return -1

deadends = ["8888"]
target = "0001"
print(openLock(deadends, target))

'''
传统BFS框架从起点开始向四周扩散，遇到终点时停止；而双向BFS则是从起点和终点同时开始扩散，当两边有交集的时候停止。
传统BFS：把整棵树的节点都搜索一遍，最终找到target
双向BFS：只遍历了半棵树就出现了交集，找到了最短距离。
'''
def openLock2(deadends, target):
    deadends = set(deadends)
    q1 = set()
    q2 = set()
    visited = set()
    step = 0
    q1.add('0000')
    q2.add(target)

    while q1 and q2:
        temp = set()
        for cur in q1:
            if cur in deadends:
                continue
            if cur in q2:
                return step
            visited.add(cur)

            for i in range(4):
                add_str = addOne(cur, i)
                if not add_str in visited:
                    temp.add(add_str)
                sub_str = subOne(cur, i)
                if not sub_str in visited:
                    temp.add(sub_str)
        step += 1
        q1, q2 = q2, temp
    return -1

    
'''
双向BFS的优化说明：
（1）无论传统BFS还是双向BFS，无论是否优化，从Big O衡量标准来看，时间复杂度时一样的。
（2）双向BFS是一种trick，算法运行的速度会相对快一点
按照BFS，队列/集合中的元素越多，扩散之后新的队列/集合中的元素就越多；
在双向BFS算法中，如果我们每次都选择一个较小的集合进行扩散，那么占用的空间增长速度就会慢一些，效率就会高一点。
'''

def openLock3(deadends, target):
    deadends = set(deadends)
    q1 = set()
    q2 = set()
    visited = set()
    step = 0
    q1.add('0000')
    q2.add(target)

    while q1 and q2:
        if len(q1) > len(q2):
            q1, q2 = q2, q1 
        temp = set()
        for cur in q1:
            if cur in deadends:
                continue
            if cur in q2:
                return step
            visited.add(cur)

            for i in range(4):
                add_str = addOne(cur, i)
                if not add_str in visited:
                    temp.add(add_str)
                sub_str = subOne(cur, i)
                if not sub_str in visited:
                    temp.add(sub_str)
        step += 1
        q1, q2 = q2, temp
    return -1

