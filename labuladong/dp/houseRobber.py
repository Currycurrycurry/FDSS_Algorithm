# 198. 打家劫舍
# 时间复杂度N 空间复杂度N
def rob(self, nums) -> int:
    if len(nums) == 0:
        return 0
    dp = [0] * (len(nums) + 1)
    dp[1] = nums[0] 
    for i in range(2, len(nums) + 1, 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
    return dp[-1]

# 时间复杂度N 空间复杂度1
def rob(self, nums) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * 3
    dp[1] = nums[0] 
    for i in range(2, len(nums) + 1, 1):
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        dp[2] = max(dp[1], dp[0] + nums[i - 1] )
        dp[0] = dp[1]
        dp[1] = dp[2]
    return dp[2]

# 213. 打家劫舍 II (环形数组)
def rob(self, nums) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    dp1 = [0] * (len(nums) - 1)
    dp2 = [0] * (len(nums) - 1)
    dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
    dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
    for i in range(2, len(nums) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])   
    return max(dp1[-1], dp2[-1])

# 337. 打家劫舍 III （二叉树）
def rob(self, root) -> int:
    memo = dict()
    def traverse(root):
        if not root:
            return 0
        if root in memo.keys():
            return memo[root]
        rob_it = root.val
        if root.left:
            rob_it += traverse(root.left.left) + traverse(root.left.right)
        if root.right:
            rob_it += traverse(root.right.left) + traverse(root.right.right)
        not_rob = traverse(root.left) + traverse(root.right)
        memo[root] = max(rob_it, not_rob)
        return memo[root]
    return traverse(root)

