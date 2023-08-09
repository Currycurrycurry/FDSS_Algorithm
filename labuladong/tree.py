# 【快速排序】就是个二叉树的【前序遍历】，【归并排序】就是个二叉树的【后序遍历】
# 本质上是利用【递归的堆栈】帮你实现了【倒序遍历】的效果。
###############
# 二叉树题目的递归解法可以分两类思路，第一类是遍历一遍二叉树得出答案，
# 第二类是通过分解问题计算出答案，这两类思路分别对应着 回溯算法核心框架 和 动态规划核心框架。
###############
# 【前中后序】是遍历二叉树过程中处理每一个节点的【三个特殊时间点】
#【前序】执行：自顶向下
# 前序位置的代码在刚刚进入一个二叉树节点的时候执行；
# 前序位置的代码只能从【函数参数】中获取【父节点】传递来的数据
# 本身其实没有什么特别的性质，之所以你发现好像很多题都是在前序位置写代码，
# 实际上是因为我们习惯把那些对前中后序位置不敏感的代码写在前序位置罢了。
# 【后序】执行：自底向上
# 后序位置的代码在将要离开一个二叉树节点的时候执行；
# 后序位置的代码不仅可以获取【参数数据】，还可以获取到【子树】通过【函数返回值】传递回来的数据。
# 一旦你发现题目和【子树】有关，那大概率要给函数设置【合理的定义和返回值】，在【后序】位置写代码了。
# 中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。
###############
# 【核心】二叉树的所有问题，就是让你在前中后序位置注入巧妙的代码逻辑，去达到自己的目的。
# 你只需要单独思考每一个节点应该做什么，其他的不用你管。
# 抛给二叉树遍历框架，递归会在所有节点上做相同的操作。


# 普通二叉树节点-Node
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

# 有父节点的二叉树节点-SpecialTreeNode
class SpecialTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# 三叉树节点-ThreeNode
class ThreeNode(Node):
    def __init__(self, val):
        Node.__init__(self, val)
        self.mid = None

# N叉树节点-TreeNNode
class TreeNNode:
    def __init__(self, val):
        self.val = val
        self.chi

# 四叉树节点
class Tree4Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# 104. 二叉树的最大深度
def maxDepth(root):
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0

# 222. 【完全二叉树】的节点总数
# 【完全二叉树】Complete Binary Tree，每一层都是紧凑靠左排列的
# 【满二叉树】Perfect Binary Tree，是一种特殊的完全二叉树，每层都是是满的，像一个稳定的三角形
# 英文中的Full Binary Tree：指一棵二叉树的所有节点要么没有孩子节点，要么有两个孩子节点
# 一棵完全二叉树的两棵子树，至少有一棵是满二叉树.
def countNodes(root) -> int:
    if not root:
        return 0
    left_height, right_height = 0, 0
    left_node, right_node = root, root
    while left_node:
        left_node = left_node.left
        left_height += 1
    while right_node:
        right_node = right_node.right
        right_height += 1
    if left_height == right_height:
        return 2 ** left_height - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

# 98. 验证二叉搜索树-普通递归
def isValidBST1(root):
    def dfs(root, lower_bound, upper_bound):
        if not root:
            return True
        return lower_bound < root.val < upper_bound \
        and dfs(root.left, lower_bound, root.val) \
        and dfs(root.right, root.val, upper_bound)
    dfs(root, -float('inf'), float('inf'))

# 98. 验证二叉搜索树-中序递归
def isValidBST2(root):
    global pre
    pre = None
    if not root:
        return True
    if not isValidBST2(root.left):
        return False
    global pre
    if pre is not None and root.val <= pre:
        return False
    pre = root.val
    return isValidBST2(root.right)

# 98. 验证二叉搜索树-中序迭代
def isValidBST3(root):
    stack, inorder = [], float('-inf')
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= inorder:
            return False
        inorder = root.val
        root = root.right
    return True

# （难）95. 不同的二叉搜索树（2）
'''
时间复杂度：
卡特兰数：n个点生成的二叉搜索树的数目G(n)
每棵二叉搜索树建树时间：O(n)
总时间复杂度为O(n*G(n))
空间复杂度：
与时间复杂度相同
'''
def generateTrees(n):
    def generateTree(start, end):
        # base case 
        if start > end:
            return [None,]
        all_trees = []
        # iterate all root nodes, i
        for i in range(start, end+1):
            left_trees = generateTree(start, i-1)
            right_trees = generateTree(i+1, end)
            # construct the tree
            for l in left_trees:
                for r in right_trees:
                    root = Node(i)
                    root.left = l
                    root.right = r
                    all_trees.append(root)
        return all_trees
    return generateTree(1, n) if n > 0 else []

# 96. 不同的二叉搜索树的个数(动态规划)
'''
假设n个节点存在二叉排序树的个数是G(n)，
1为根节点，2为根节点，...，n为根节点，
当1为根节点时，其左子树节点个数为0，右子树节点个数为n-1，
同理当2为根节点时，其左子树节点个数为1，右子树节点为n-2，
所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
'''
def numTrees(n):
    G = [0] * (n+1)
    G[0], G[1] = 1, 1
    for i in range(2,n+1):
        for j in range(n):
            G[i] += G[j] * G[i-j-1]
    return G[n]

# 99. 恢复二叉搜索树
def recoverBST(root):
    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    
    def findTwoNodes(nums):
        n = len(nums)
        x = y = -1
        for i in range(n - 1):
            if nums[i+1] < nums[i]:
                y = nums[i + 1]
                if x == -1:
                    x = nums[i]
                else:
                    break
        return [x, y]

    def recover(node_list, root, count):
        if root:
            if root.val == node_list[0] or root.val == node_list[1]:
                root.val = node_list[1] if root.val == node_list[0] else node_list[0]
                count -= 1
                if count == 0:
                    return
            recover(node_list, root.left, count)
            recover(node_list, root.right, count)
    recover(findTwoNodes(inorder(root)), root, 2)

def recoverTree(self, root):
    # 用两个变量x，y来记录需要交换的节点
    self.x = None
    self.y = None
    self.pre = None
    # 中序遍历二叉树，并比较上一个节点(pre)和当前节点的值，如果pre的值大于当前节点值，则记录下这两个节点
    def dfs(root):
        if not root:
            return
        dfs(root.left)
        if not self.pre:
            self.pre = root
        else:
            if self.pre.val>root.val:
                self.y = root
                if not self.x:
                    self.x = self.pre
            self.pre = root
        dfs(root.right)
    dfs(root)
    # 如果x和y都不为空，说明二叉搜索树出现错误的节点，将其交换
    if self.x and self.y:
        self.x.val,self.y.val = self.y.val,self.x.val


# 993. 二叉树的堂兄弟节点
def isCousin(root, x, y):
    def getPath(root, val, path=[]):
            if not root:
                return False
            path.append(root.val)
            if root.val == val:
                return True
            left = getPath(root.left, val, path)
            right = getPath(root.right, val, path)
            if left or right:
                return True
            path.pop()
    list1 = []
    list2 = []
    getPath(root, x, list1)
    getPath(root, y, list2)
    return len(list1) == len(list2) and list1[list1.index(x) - 1] != list2[list2.index(y) - 1]

# 993. 二叉树的堂兄弟节点 只记录parent
def isCousin2(root, x, y):
    parent = {}
    depth = {}
    def dfs(node, par = None):
        if node:
            depth[node.val] = 1 + depth[par.val] if par else 0
            parent[node.val] = par
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)
    return depth[x] == depth[y] and parent[x] != parent[y]

# 1519. 子树中标签相同的节点数
def countSubTrees(n, edges, labels):
    pass

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

# 迭代前序 n叉树版
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

# 迭代前序 二叉树版
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

# 镜像版前序遍历
def inorder_loop(root):
    stack, res = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

# 与中序的不同之处在于：
# 中序遍历中，从栈中弹出的节点，其左子树是访问完了，可以直接访问该节点，然后接下来访问右子树。
# 后序遍历中，从栈中弹出的节点，我们只能确定其左子树肯定访问完了，但是无法确定右子树是否访问过。
# 因此，我们在后序遍历中，引入了一个prev来记录历史访问记录。
# 当访问完一棵子树的时候，我们用prev指向该节点。
# 这样，在回溯到父节点的时候，我们可以依据prev是指向左子节点，还是右子节点，来判断父节点的访问情况。

def postorder_loop(root):
    if not root:
        return []
    stack, res = [], []
    prev = None # 用prev来记录访问历史，在回溯到父节点时，可以由此来判断，上一个访问的节点是否为右子树
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        # 从栈中弹出的元素，左子树一定是访问完了的
        root = stack.pop()
        # 如果没有右子树，或者右子树访问完了，也就是上一个访问的节点是右子节点时
        # 说明可以访问当前节点
        if not root.right or root.right == prev:
            res.append(root.val)
            # 更新历史访问记录，这样回溯的时候父节点可以由此判断右子树是否访问完成
            prev = root
            root = None
        else:
            # 如果右子树没有被访问，那么将当前节点压栈，访问右子树
            stack.append(root)
            root = root.right
    return res

def mirror_preorder(root):
    return [root.val] + preorder(root.right) + preorder(root.left) if root else []

# 判断BST是否是前序遍历
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

def inorder_normal(root):
    res = []
    def dfs(root, res):
        if root:
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
    dfs(root, res)
    return res



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

def levelorder1(root):
    if not root:
        return []
    heap = [root]
    ans = []
    while len(heap) > 0:
        cnt = len(heap)
        tmp = []
        for i in range(cnt):
            node = heap.pop(0)
            tmp.append(node.val)
            if node.left:
                heap.append(node.left)
            if node.right:
                heap.append(node.right)
        ans.append(tmp)
    return ans

def levelorder2(root):
    if not root:
        return []
    heap = [root]
    ans = []
    while len(heap) > 0:
        node = heap.pop(0)
        ans.append(node.val)
        if node.left:
            heap.append(node.left)
        if node.right:
            heap.append(node.right)
    return ans

def mirror_levelorder(root):
    if not root:
        return []
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

def mirror_levelorder2(root):
    if not root:
        return []
    res = []
    heap = [root]
    while len(heap) > 0:
        cnt = len(heap)
        tmp = []
        for i in range(cnt):
            node = heap.pop(0)
            tmp.append(node.val)
            if node.right:
                heap.append(node.right)
            if node.left:
                heap.append(node.left)
        res.append(tmp)
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

# 236. 二叉树的最近公共祖先
# LCA问题
# 最近公共祖先节点的左右子树一定分别包含着两个节点：
def lowestCommonAncestor(self, root, p, q):
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right 

# the least common ancester(LCA) of the two node
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

# 633 打印二叉树
def printTree(root):
    def getHeight(root):
        return max(getHeight(root.right), getHeight(root.left)) + 1 if root else 0
    def fill(res, root, level, left, right):
        if root:
            res[level][(left + right) // 2] = str(root.val)
            fill(res, root.left, level + 1, left, (left + right) // 2)
            fill(res, root.right, level + 1, (left + right) // 2 + 1, right)
    height = getHeight(root)
    width = pow(2, height) - 1
    res = [[""] * width for i in range(height)]
    fill(res, root, 0, 0, width - 1)
    return res

# 427. 建立四叉树
def construct(self, grid):
    if not grid:
        return Tree4Node(False, False, None, None, None, None)
    length, val, pure = len(grid), 0, True
    for line in grid:
        for n in line:
            val += n
            if not n:
                pure = False
    if val and pure:
        return Tree4Node(True, True, None, None, None, None)
    if val == 0:
        return Tree4Node(False, True, None, None, None, None)
    mid = length >> 1
    tl, tr, bl, br = [], [], [], []
    for line in grid[:mid]:
        tl.append(line[:mid])
        tr.append(line[mid:])
    for line in grid[mid:]:
        bl.append(line[:mid])
        br.append(line[mid:])
    return Node(val=False, isLeaf=False, 
    topLeft=self.construct(tl), 
    topRight=self.construct(tr), 
    bottomLeft=self.construct(bl), 
    bottomRight=self.construct(br)
    )
    
# 124. 二叉树中的最大路径和
class Solution:
    def __init__(self):
        self.maxSum = -float('inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
        
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)
   
        maxGain(root)
        return self.maxSum



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
print('-------------')
print('max depth is {}'.format(maxDepth(root)))
nums1 = [1, 4, 3, 7, 6, 5]
nums2 = [5, 3, 1, 4, 6, 7]
nums3 = [1, 2, 3, 4, 5, 6, 7]
print('{nums} isPostorder: {ans}'.format(nums=nums1, ans=isPostorder(nums1)))
print('{nums} isPostorder: {ans}'.format(nums=nums2, ans=isPostorder(nums2)))
print('{nums} isPreorder: {ans}'.format(nums=nums1, ans=isPreorder(nums1)))
print('{nums} isPretorder: {ans}'.format(nums=nums2, ans=isPreorder(nums2)))
print('{nums} isPretorder: {ans}'.format(nums=nums3, ans=isPreorder(nums3)))

