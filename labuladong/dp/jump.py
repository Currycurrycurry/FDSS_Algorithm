from typing import List
from collections import Counter
# 55. 跳跃游戏
# 每一步都计算一下从当前位置最远能够跳到哪里，然后和一个全局最优的最远位置 farthest 做对比。
# 通过每一步的最优解，更新全局最优解，这就是贪心。
def canJump(nums) -> bool:
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        # 防止当前value为0而卡住
        if farthest <= i:
            return False
    return farthest >= len(nums) - 1

# 45. 跳跃游戏 II
# 第一次跳跃游戏：带备忘录的递归 时间复杂度n2 空间复杂度n
def jump(nums: List[int]) -> int:
    n = len(nums)
    memo = [n for _ in range(len(nums))]
    def dp(i):
        if i >= n - 1:
            return 0
        if memo[i] != n:
            return memo[i]
        step = nums[i]
        sub_problem = n
        for j in range(1, step + 1):
            sub_problem = min(sub_problem,  dp(i + j) + 1)
        memo[i] = sub_problem
        return sub_problem
    return dp(0)

# 第二次跳跃游戏：DP数组法 时间复杂度n2 空间复杂度n
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    # 定义dp数组：到达i所使用的最少跳跃次数
    dp = [n for _ in range(n)]
    # base case
    dp[0] = 0
    # core transition:
    for i in range(1, n):
        for j in range(i):
            if j + nums[j] >= i: # 一旦超过当前index就更新dp
                dp[i] = min(dp[i], 1 + dp[j])
    return dp[-1]

# 第三次跳跃游戏：贪心算法
def jump(nums: List[int]) -> int:
    # 2 3 1 1 4 
    n = len(nums)
    end = 0
    farthest = 0
    cnt = 0
    for i in range(0, n - 1):
        farthest = max(farthest, nums[i] + i)
        if i == end:
            cnt += 1
            end = farthest
    return cnt

# 659. 分割数组为连续子序列
def isPossible(self, nums: List[int]) -> bool:
    num_counter = Counter(nums)
    tails = [0 for _ in range(max(nums)+1)]
    length = len(nums)
    for i in range(length):
        if num_counter[nums[i]] == 0:
            continue
        elif nums[i] - 1 >= 0 and num_counter[nums[i]] > 0 and tails[nums[i]-1] > 0:
            num_counter[nums[i]] -= 1
            tails[nums[i]-1] -= 1
            tails[nums[i]] += 1
        elif nums[i] + 1 <= max(nums) and nums[i] + 2 <= max(nums) and num_counter[nums[i]] > 0 and num_counter[nums[i]+1] > 0 and num_counter[nums[i]+2] > 0:
            num_counter[nums[i]] -= 1
            num_counter[nums[i]+1] -= 1
            num_counter[nums[i]+2] -= 1
            tails[nums[i]+2] += 1
        else:
            return False
        
    return True