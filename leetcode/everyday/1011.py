class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_value = sum(nums)
        if sum_value % 2 != 0 or max(nums) > sum_value:
            return False
        target = sum_value // 2
        dp = [True] + [False for _ in range(target)]
        for num in nums:
            for j in range(target, num - 1, -1):
                if not dp[j]:
                    dp[j] = dp[j - num]
        return dp[-1]
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, visited, sum, target):
            nonlocal res
            if res:
                return
            if sum == target:
                res = True
                return 
            if sum > target:
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i] and not visited[i - 1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    dfs(nums, visited, sum + nums[i], target)
                    visited[i] = False
        sum_value = sum(nums)
        if sum_value % 2 != 0 or max(nums) > sum_value:
            return False
        target = sum_value // 2
        visited = [False for _ in range(len(nums))]
        res = False
        dfs(nums, visited, 0, target)
        return res

