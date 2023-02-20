# 前缀和
# 场景：原始数组不会被修改的情况下，频繁查询某个区间的累加和。
# 哈希表优化
# 304. 二维区域和检索 - 矩阵不可变
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            M, N = 0, 0
        else:
            M, N = len(matrix), len(matrix[0])
        self.pre_sum = [[0] * (N + 1) for _ in range(M + 1)]
        print(self.pre_sum)
        for i in range(M):
            for j in range(N):
                self.pre_sum[i+1][j+1] = self.pre_sum[i+1][j] + self.pre_sum[i][j+1] - self.pre_sum[i][j] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2+1][col2+1] - self.pre_sum[row2+1][col1] - self.pre_sum[row1][col2+1] + self.pre_sum[row1][col1]


def subarraySum(nums, k):
    preSum = [0]
    tmp_sum = 0
    ans = 0
    for i in nums:
        tmp_sum += i
        preSum.append(tmp_sum)
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums), 1):
                if preSum[j] - preSum[i] == k:
                    ans += 1
    return ans

def subarraySum_optimized(nums, k):
    preSum = [0]
    tmp_sum = 0
    ans = 0
    for i in nums:
        tmp_sum += i
        preSum.append(tmp_sum)
    preSum_times = dict()
    preSum_times[0] = 1
    sum0_i = 0
    for i in range(len(nums)):
        sum0_i += nums[i]
        sum0_j = sum0_i - k
        if preSum.get(sum0_j):
            ans += preSum.get(sum0_j)
        preSum.put(sum0_i, (preSum.get(sum0_i) or 0) + 1)
    return ans

# 53. 最大子数组和——前缀和做法
def maxSubArray(nums) -> int:
    n = len(nums)
    pre_sum = [0 for _ in range(n+1)]
    for i in range(n):
        pre_sum[i+1] = pre_sum[i] + nums[i]
    res = - float('inf')
    min_sum = float('inf')
    for i in range(n):
        min_sum = min(min_sum, pre_sum[i])
        res = max(res, pre_sum[i+1] - min_sum)
    return res

    

    