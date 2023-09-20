# 【单调栈】题目汇总
# 42接雨水
# 85最大矩形
# 739每日温度
# 496下一个更大元素
# 316去除重复字母
# 901股票价格跨度
# 402移掉k位数字
# 581最短无序连续子数组
# 84柱状图中最大的矩形


# 11. 盛最多水的容器
def maxArea(self, height: List[int]) -> int:
    max_value = 0
    left, right = 0, len(height) - 1
    while left < right:
        max_value = max(max_value, (right - left) * min(height[right], height[left]))
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return max_value

# 42接雨水 预计算 时间O(n) 空间O(n)
def trap(self, height: List[int]) -> int:
    res = 0
    length = len(height)
    left_max = [max(height[:i]) for i in range(1, length - 1)]
    right_max = [max(height[i:]) for i in range(1, length - 1)]
    for i in range(1, length-1):
        min_max = min(left_max[i-1], right_max[i-1])
        if height[i] < min_max:
            res += min_max - height[i]
    return res

# 42接雨水 双指针 时间O(n) 空间O(1)
def trap(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    l_max, r_max = 0, 0
    res = 0
    while left < right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            res += l_max - height[left]
            # extend up -250
            # <div class="img-content"><img src="/images/接雨水/5.jpg" class="myimage"/></div>
            left += 1
        else:
            res += r_max - height[right]
            right -= 1
    return res

# 84. 柱状图中最大的矩形
def largestRectangleArea(self, heights: List[int]) -> int:
    heights = [0] + heights + [0]
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            max_area = max(max_area, (i - stack[-1] - 1) * h)
        stack.append(i)
    return max_area

# 85最大矩形
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    m = len(matrix)
    if m == 0: return 0
    n = len(matrix[0])
    heights = [0] * n
    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "0":
                heights[j] = 0
            else:
                heights[j] += 1
        ans = max(ans, self.largestRectangleArea(heights))
    return ans


# Google面试题
def next_google(nums):
    mono_stack = []
    res = [-1 for _ in range(len(nums))]
    for i in range(len(nums)):
        while mono_stack and nums[mono_stack[-1]] < nums[i]:
            res[mono_stack[-1]] = i-mono_stack[-1]
            mono_stack.pop()
        mono_stack.append(i)
    return res

# N头牛问题
def nCow(nums):
    mono_stack = []
    res = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        while mono_stack and nums[mono_stack[-1]] < nums[i]:
            res[mono_stack[-1]] = i-mono_stack[-1]
            mono_stack.pop()
        mono_stack.append(i)
    return sum(res)

nums = [1,2,1]
print(next_google(nums))
print(nCow(nums))

# 单调栈模板
def nextGreaterElement(nums: List[int]) -> List[int]:
    n = len(nums)
    # 存放答案的数组
    res = [0 for _ in range(n)]
    s = [] 
    # 倒着往栈里放
    for i in range(n - 1, -1, -1):
        # 判定个子高矮
        while s and s[-1] <= nums[i]:
            # 矮个起开，反正也被挡着了。。。
            s.pop()
        # nums[i] 身后的更大元素
        res[i] = s[-1] if s else -1
        s.append(nums[i])
    return res

# leetcode496 下一个更大元素
# 暴力求解O(n2)
# 特殊：大数组 小数组 
# 因为题目说 nums1 是 nums2 的子集，那么我们先把 nums2 中每个元素的下一个更大元素算出来存到一个映射里，
# 然后再让 nums1 中的元素去查表即可：
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreater(nums: List[int]) -> List[int]:
        # 实现代码
        pass
    greater = nextGreater(nums2)
    greaterMap = {}
    for i in range(len(nums2)):
        greaterMap[nums2[i]] = greater[i]
    res = [0] * len(nums1)
    for i in range(len(nums1)):
        res[i] = greaterMap[nums1[i]]
    return res

# 739每日温度
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    res = [0] * n
    # 这里放元素索引，而不是元素
    s = []
    # 单调栈模板
    for i in range(n-1, -1, -1):
        while s and temperatures[s[-1]] <= temperatures[i]:
            s.pop()
        # 得到索引间距
        res[i] = s[-1] - i if s else 0
        # 将索引入栈，而不是元素
        s.append(i)
    return res

# leetcode503
# 特殊：循环数组搜索
def nextGreaterElement2(nums):
    origin_length = len(nums)
    nums = nums + nums[:-1]
    stack = []
    res = [-1 for _ in range(len(nums))]
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack[-1]] = nums[i]
            stack.pop()
        stack.append(nums[i])
    return res[:origin_length]

# leetcode556
# 下一个元素 ：下一个排列


# RMQ问题

