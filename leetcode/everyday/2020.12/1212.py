# 摆动序列
# 算出一个序列摆动子序列的最大长度
# 算出一个序列的波峰和波谷的数目


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])          
        return res


