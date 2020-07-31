# 前缀和
# 哈希表优化

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


    

    