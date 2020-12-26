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

# leetcode496 下一个更大元素
# 特殊：大数组 小数组
def nextGreaterElement(nums1, nums2):
    ans_dict = dict()
    stack = []
    for i in range(len(nums2)):
        while stack and stack[-1] < nums2[i]:
            ans_dict[stack[-1]] = nums2[i]
            stack.pop()
        stack.append(nums2[i])
    while stack:
        ans_dict[stack.pop()] = -1
    return [ans_dict[num] for num in nums1]

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

# leetcode84 柱状图中最大的矩形
def get_max_matrix(heights):
    heights = [0] + heights + [0]
    max_area = 0
    stack = []
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack[-1]]
            max_area = max(max_area, (i - stack[-1] - i) * h)
        stack.append(i)
    return max_area

# leetcode85 最大矩形
def get_max_matrix2(matrix):
    if not matrix: 
        return 0
    row_len, col_len = len(matrix), len(matrix[0])
    height = [0 for _ in range(col_len)]
    max_area = 0
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0
        max_area = max(max_area, get_max_matrix(height))
    return max_area

# RMQ问题

