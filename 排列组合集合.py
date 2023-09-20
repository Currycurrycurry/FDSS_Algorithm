# 排列/组合/子集问题的九种变化

############################# 排列 #############################
# 46. 全排列
class Solution:
    res = []
    #记录回溯算法的递归路径
    track = []
    # track 中的元素会被标记为 true
    used = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res

    # 回溯算法核心函数
    def backtrack(self, nums):
        # base case，到达叶子节点
        if len(self.track) == len(nums):
            # 收集叶子节点上的值
            self.res.append(self.track[:])
            return

        # 回溯算法标准框架
        for i in range(len(nums)):
            # 已经存在 track 中的元素，不能重复选择
            if self.used[i]:
                continue
            # 做选择
            self.used[i] = True
            self.track.append(nums[i])
            # 进入下一层回溯树
            self.backtrack(nums)
            # 取消选择
            self.track.remove(nums[i])
            self.used[i] = False

# 47 「全排列 II」：给你输入一个可包含重复数字的序列 nums，请你写一个算法，返回所有可能的全排列
def backtrack(nums: List[int], track: LinkedList[int]):
    # add type annotation on function params and reserve comments
    # 初始化
    # used 存储已经选择过的下标 i，避免重复选择
    # res 用于存储结果
    used = set()
    res = []

    # 递归回溯函数定义
    def dfs():
        # 到达叶子结点后，记录并返回
        if len(track) == len(nums):
            # 注意要加[:]
            res.append(track[:])
            return

        # 记录之前树枝上元素的值
        # 题目说 -10 <= nums[i] <= 10，所以初始化为特殊值
        prev_num = -666
        for i in range(len(nums)):
            # 排除不合法的选择
            if i in used or nums[i] == prev_num:
                continue

            # 做出选择
            track.append(nums[i])
            used.add(i)
            # 记录这条树枝上的值
            prev_num = nums[i]

            # 进入下一层决策树
            dfs()

            # 取消选择
            track.removeLast()
            used.remove(i)
    # 驱动函数
    dfs()
    return res

############################# 组合 #############################
# 77. 组合
def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    nums = [i for i in range(1, n+1)]
    def helper(start, path):
        if len(path) == k:
            res.append(path)
        for i in range(start, len(nums)):
            helper(i + 1, path + [nums[i]])
    helper(0, [])
    return res

# 77. 组合 套用模板
class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start: int, n: int, k: int) -> None:
        # base case
        if k == len(self.track):
            # 遍历到了第 k 层，收集当前节点的值
            self.res.append(self.track.copy())
            return
        
        # 回溯算法标准框架
        for i in range(start, n+1):
            # 选择
            self.track.append(i)
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(i + 1, n, k)
            # 撤销选择

# 40. 组合总和——找到所有目标和的组合
class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录 track 中的元素之和
        self.trackSum = 0
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        # 先排序，让相同的元素靠在一起
        candidates.sort()
        self.backtrack(candidates, 0, target)
        return self.res
    
    # 回溯算法主函数
    def backtrack(self, nums: List[int], start: int, target: int):
        # base case，达到目标和，找到符合条件的组合
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        # base case，超过目标和，直接结束
        if self.trackSum > target:
            return
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的树枝，只遍历第一条
            if i > start and nums[i] == nums[i - 1]:
                continue
            # 做选择
            self.track.append(nums[i])
            self.trackSum += nums[i]
            # 递归遍历下一层回溯树
            self.backtrack(nums, i + 1, target)
            # 撤销选择
            self.track.pop()
            self.trackSum -= nums[i]

# 39. 组合总和——无重复元素但同一个数字可以无限制重复被选取
class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录 track 中的路径和
        self.trackSum = 0

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return self.res
        self.backtrack(candidates, 0, target)
        return self.res

    # 回溯算法主函数
    def backtrack(self, nums: List[int], start: int, target: int) -> None:
        # base case，找到目标和，记录结果
        if self.trackSum == target:
            self.res.append(list(self.track))
            return None
        # base case，超过目标和，停止向下遍历
        if self.trackSum > target:
            return None

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 选择 nums[i]
            self.trackSum += nums[i]
            self.track.append(nums[i])
            # 递归遍历下一层回溯树
            # 区别点：【同一元素可重复使用】，注意参数
            self.backtrack(nums, i, target)
            # 撤销选择 nums[i]
            self.trackSum -= nums[i]
            self.track.pop()



############################# 子集 #############################


# 78. 子集
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def helper(start, path):
        res.append(path)
        for i in range(start, len(nums)):
            helper(i + 1, path + [nums[i]])
    helper(0, [])
    return res

# 78. 子集 套用模板
class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:  
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track)) 
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()


            self.track.pop()

# 90. 子集 II 可能包含重复元素（因此需要剪枝）
class Solution:
    def __init__(self):
        # 用来存储结果的列表
        self.res = []
        # 用来存储当前走过的路径
        self.track = []
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 对给定的数组进行排序，这样相同的元素就会排在一起。
        nums.sort()
        # 对数组进行回溯
        self._backtrack(nums, 0)
        return self.res
    
    def _backtrack(self, nums, start):
        # 前序位置，每个节点的值都是一个子集
        self.res.append(self.track[:])
        # 从start开始遍历nums数组
        for i in range(start, len(nums)):
            # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
            if i > start and nums[i] == nums[i-1]:
                continue
            # 把当前数值添加到走过的路径列表中
            self.track.append(nums[i])
            # 从下一个数字的位置继续回溯
            self._backtrack(nums, i+1)
            # 回溯过程中要把当前数值从走过的路径中移除
            self.track.pop()

############################# N皇后 #############################
class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board: List[List[str]], row: int) -> None:
        if row == len(board):
            self.res.append([row[:] for row in board])
            return
      
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            
            board[row][col] = "Q"
            self.backtrack(board, row + 1)
            board[row][col] = "."

    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列是否有皇后冲突
        for i in range(n):
            if board[i][col] == "Q":
                return False
        
        # 检查右上方是否有皇后冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
    
        # 检查左上方是否有皇后冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        return True

# 698. 划分为k个相等的子集
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k:
        return False
    size = sum(nums) / k
    used = 0
    memo = dict()
    def recurse(used, start, bucket, k, memo):
        if k == 0:
            return True
        if bucket == size:
            res = recurse(used, 0, 0, k - 1, memo)
            memo[used] = res
            return res
        if used in memo:
            return memo[used]
        for i in range(start, len(nums)):
            if ((used >> i) & 1) == 1:
                continue
            if nums[i] + bucket > size:
                continue
            used |= 1 << i
            bucket += nums[i]
            if recurse(used, i+1, bucket, k, memo):
                return True
            used ^= 1 << i
            bucket -= nums[i]
        return False
    return recurse(used, 0, 0, k, memo)