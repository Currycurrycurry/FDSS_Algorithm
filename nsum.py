# 1. 两数之和 字典版 时间O(n) 空间O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_index = dict()
    for i, num in enumerate(nums):
        if (target - num) in num_index.keys() :
            return (num_index[target- num], i)
        else:
            num_index[num] = i
    return -1

# 1. 两数之和 排序双指针版 时间O(nlgn) 空间O(1)


# 167. 两数之和 II - 输入有序数组 因为有序所以直接双指针 时间O(n) 空间O(1)
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start < end:
        if (numbers[start] + numbers[end]) == target:
            return [start + 1, end + 1]
        elif (numbers[start] + numbers[end]) < target:
            start += 1
        else:
            end -= 1
    return [start + 1, end + 1]

# 15. 三数之和 总的时间复杂度就是 O(NlogN + N^2) = O(N^2)
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # sorted nums
    def twoSum(nums, target):
        res = []
        left, right = 0, len(nums) - 1
        while left < right:
            left_num, right_num = nums[left], nums[right]
            tmp_sum = left_num + right_num
            if tmp_sum == target:
                res.append([left_num, right_num])
                while left < len(nums) and nums[left] == left_num:
                    left += 1
                while right >= 0 and nums[right] == right_num:
                    right -= 1
            elif tmp_sum < target:
                while left < len(nums) and nums[left] == left_num:
                    left += 1
            elif tmp_sum > target:
                while right >= 0 and nums[right] == right_num:
                    right -= 1
        return res 

    nums.sort()
    start, end = 0, len(nums) - 1
    i = 0
    ans = []
    # enumerate the first num
    while i < end:
        two_values = twoSum(nums[i+1:], -nums[i])
        for two_value in two_values:
            ans.append([nums[i]] + two_value)
        while i + 1 <= end and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return ans

# 18. 四数之和 直接调用三数之和的结果 时间O(N^3)
def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    start, end = 0, len(nums) - 1
    i = 0
    ans = []
    # enumerate the first num
    while i < end:
        three_values = threeSum(nums[i+1:], target-nums[i]) # 直接调用上面的函数
        for three_value in three_values:
            ans.append([nums[i]] + three_value)
        while i + 1 <= end and nums[i] == nums[i + 1]:
            i += 1
        i += 1
    return ans


# 1995. 统计特殊四元组
## 时间O(n^4) 空间O(1)
def countQuadruplets(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        ans += 1
    return ans

## 引入字典对时间复杂度优化：时间O(n^3) 空间O(min(n, C))
def countQuadruplets(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    cnt = Counter()
    for c in range(n - 2, 1, -1):
        cnt[nums[c + 1]] += 1
        for a in range(c):
            for b in range(a + 1, c):
                if (total := nums[a] + nums[b] + nums[c]) in cnt:
                    ans += cnt[total]
    return ans

