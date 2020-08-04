# 普通二叉树节点 
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

# 有父节点的二叉树节点
class SpecialTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# 三叉树节点
class ThreeNode(Node):
    def __init__(self, val):
        Node.__init__(self, val)
        self.mid = None

# N叉树节点
class TreeNNode:
    def __init__(self, val):
        self.val = val
        self.children = []
    
def build3aryTree(arr):
    pass

# 【树的遍历-基础框架型问题】二叉树的前序、中序、后序、层序遍历相关问题
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def preorder_n(root):
    res = []
    def helper(root):
        if root:
            for child in root.children:
                res.append(child.val)
    helper(root)
    return res

# 迭代前序
def preorder_loop_n(root):
    if root:
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans
    return []

def preorder_loop(root):
    ans = []
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return ans

            
def mirror_preorder(root):
    return [root.val] + preorder(root.right) + preorder(root.left) if root else []

def isPreorder(nums):
    length = len(nums)
    if nums:
        root = nums[0]
        left = 1
        while left <= length - 1 and nums[left] < root:
            left += 1
        right = left
        while right <= length - 1:
            if nums[right] < root:
                return False
            right += 1
        left_part = True if left == 1 else isPreorder(nums[1:left])
        right_part = True if right == left else isPreorder(nums[left:right])
        return left_part and right_part
    return False


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def mirror_inorder(root):
    return inorder(root.right) + [root.val] + inorder(root.left) if root else []

def isInorder(nums):
    pass

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

def mirror_postorder(root):
    return postorder(root.right) + postorder(root.left) + [root.val] if root else []

def isPostorder(nums):
    length = len(nums)
    if nums:
        root = nums[-1]
        left = 0
        while nums[left] < root:
            left += 1
        right = left
        while right < length - 1:
            if nums[right] < root:
                return False
            right += 1
        left_part = True if left == 0 else isPostorder(nums[:left])
        right_part = True if right == left else isPostorder(nums[left:right])
        return left_part and right_part
    return False

def levelorder(root):
    res = []
    heap = []
    heap.append(root)
    while len(heap) > 0:
        node = heap.pop(0)
        if node.left:
            heap.append(node.left)
        if node.right:
            heap.append(node.right)
        res.append(node.val)
    return res

def mirror_levelorder(root):
    res = []
    heap = []
    heap.append(root)
    while len(heap) > 0:
        node = heap.pop(0)
        if node.right:
            heap.append(node.right)
        if node.left:
            heap.append(node.left)
        res.append(node.val)
    return res

# 【综合】判断是否是树的前序/后序遍历，并建树
def buildPreTree(nums):
    if nums:
        root = Node(nums[0])
        left = 1
        while left <= len(nums) - 1 and nums[left] < nums[0]:
            left += 1
        right = len(nums)
        root.left = buildPreTree(nums[1: left])
        root.right = buildPreTree(nums[left: right])

def buildPreorderTree(nums):
    if isPreorder(nums):
        return buildPreTree(nums)
    else:
        return False

# 判断两棵树的关系
def isSameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

def isSimilarTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return isSimilarTree(root1.left, root2.left) and isSimilarTree(root1.right, root2.right)

def ifExistNode(root, node):
    if not root:
        return False
    if root == node:
        return True
    return ifExistNode(root.left, node) or ifExistNode(root.right, node)

def hasSubTree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return hasSubTree(tree1.left, tree2.left) and hasSubTree(tree1.right, tree2.right)
        else:
            return hasSubTree(tree1.left, tree2) or hasSubTree(tree1.right, tree2)
    if not tree1 and tree2:
        return False
    return True

def isSymmetric(root):
    def isSym(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)
    return isSym(root, root)

maxPath = -float('inf')
# 后序遍历
def oneSideMax(root):
    if not root:
        return 0
    left = max(0, oneSideMax(root.left))
    right = max(0, oneSideMax(root.right))
    global maxPath
    maxPath = max(maxPath, left + right + root.val)
    return max(left, right) + root.val

# 前序遍历
def buildTree(preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
    if preStart > preEnd or inStart > inEnd:
        return None
    root = Node(preorder[preStart])
    inRoot = inMap.get(root.val)
    numsLeft = inRoot - inStart
    root.left = buildTree(preorder, preStart + 1, preStart + numsLeft, inorder, inStart, inRoot - 1, inMap)
    root.right = buildTree(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inMap)
    return root


# 搜索特定值/特定路径/特定节点问题
def maxPath(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root.val
    max_num = float('inf')
    # calculate the sum of tree with this root
    def calculateSum(root):
        if root:
            return calculateSum(root.left) + root.val + calculateSum(root.right)
        return 0
    tree_sum = calculateSum(root)
    def traverse(root):
        nonlocal max_num
        if root:
            traverse(root.left)
            tree1_sum = calculateSum(root)
            if tree1_sum * (tree_sum - tree1_sum) > max_num:
                max_num = tree1_sum * (tree_sum - tree1_sum)
            traverse(root.right)
    traverse(root)
    return max_num

# 二叉树中和为某一值的路径
def find_path(tree, num):
    ret = []
    if not tree:
        return ret
    path = [tree]
    sums = [tree.val]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1]+tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()

    dfs(tree)
    return ret

# 68 the common ancester of the two node
## base case
def findPath(root, node, path):
    if not root or not node:
        return False
    path.append(root)
    if root == node:
        return True
    left = findPath(root.left, node, path)
    right = findPath(root.right, node, path)
    if left or right:
        return True
    path.pop()
    
def leastCommonNode(root, node1, node2):
    path1 = []
    path2 = []
    findPath(root, node1, path1)
    findPath(root, node2, path2)
    commonNodes = set(path1) & set(path2)
    max_index = -1
    for i in commonNodes:
        if path1.index(i) > max_index:
            max_index = path1.index(i)
    return path1[max_index]

def findKthNode1(root, k):
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    return inorder(root)[k - 1]

def findKthNode2(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right

def findKthNode3(root, k):
    count = 0
    ans = 0
    def inorder(root, k):
        nonlocal count
        nonlocal ans
        if not root:
            return None
        inorder(root.left, k)
        count += 1
        if count == k:
            ans = root.val
        else:
            inorder(root.right, k)   
    inorder(root, k)
    return ans

def findKthNode4(root, k):
    pass

# 与其他数据结构结合类问题/判断树形态问题
def convertTree2List(root):
    pass


# 根据前序遍历和中序遍历建树
def buildTreeByPreorderAndInorder(root):
    if preorder and inorder:
        root_val = preorder[0]
        root_index = 0
        while root_index < len(inorder) and inorder[root_index] != root_val:
            root_index += 1
        root = Node(root_val)
        root.left = buildTree(preorder[1:1+root_index], inorder[:root_index])
        root.right = buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root

# 331. 验证二叉树的前序序列化
def isValidSerialization(preorder):
    slots = 1
    for i in preorder.split(','):
        if slots == 0:
            return False
        slots -= 1
        if i != '#':
            slots += 2
    return slots == 0

# 889. 根据前序和后序遍历构造二叉树
def buildTreeByPreorderAndPostorder(pre, post):
    if not pre: return None
    root = Node(pre[0])
    if len(pre) == 1: return root
    L = post.index(pre[1]) + 1
    root.left = buildTreeByPreorderAndPostorder(pre[1:L+1], post[:L])
    root.right = buildTreeByPreorderAndPostorder(pre[L+1:], post[L:-1])
    return root

# (难)LCP 10. 二叉树任务调度
def minimalExecTime(root):
        def dfs(root):
            if root is None:
                return 0., 0.
            tc = root.val
			
            # 先递归左右子树
            a, b = dfs(root.left)
            c, d = dfs(root.right)
            
            tc = tc + a + c
            # 只考虑 a >= c 的情况，不满足就交换
            if a < c:
                a, c = c, a
                b, d = d, b
            
            if a - 2 * b <= c:
                pc = (a + c) / 2
            else:
                pc = c + b

            return tc, pc
        tc, pc = dfs(root)
        return tc - pc

######################################TEST######################################
nodes = [Node(i) for i in range(10)]
root = nodes[5]
root.left = nodes[3]
root.right = nodes[6]
nodes[3].left = nodes[1]
nodes[3].right = nodes[4]
nodes[6].right = nodes[7]

print('preorder: {}'.format(preorder(root)))
print('inorder: {}'.format(inorder(root)))
print('postorder: {}'.format(postorder(root)))
print('levelorder: {}'.format(levelorder(root)))
print('after mirroring:')
print('preorder: {}'.format(mirror_preorder(root)))
print('inorder: {}'.format(mirror_inorder(root)))
print('postorder: {}'.format(mirror_postorder(root)))
print('levelorder: {}'.format(mirror_levelorder(root)))
nums1 = [1, 4, 3, 7, 6, 5]
nums2 = [5, 3, 1, 4, 6, 7]
nums3 = [1, 2, 3, 4, 5, 6, 7]
print('{nums} isPostorder: {ans}'.format(nums=nums1, ans=isPostorder(nums1)))
print('{nums} isPostorder: {ans}'.format(nums=nums2, ans=isPostorder(nums2)))
print('{nums} isPreorder: {ans}'.format(nums=nums1, ans=isPreorder(nums1)))
print('{nums} isPretorder: {ans}'.format(nums=nums2, ans=isPreorder(nums2)))
print('{nums} isPretorder: {ans}'.format(nums=nums3, ans=isPreorder(nums3)))

