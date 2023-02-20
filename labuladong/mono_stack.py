# -*- coding: utf-8 -*
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
# 132模式（121模式、101模式、1423模式、……）

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

import collections

# 316. 去除重复字母
# 1081. 不同字符的最小子序列
def removeDuplicateLetters(self, s: str) -> str:
    stack = []
    counter = collections.Counter(s)
    for letter in s:
        if letter not in stack:
            while stack and stack[-1] > letter and counter[stack[-1]] != 0:
                stack.pop()
            stack.append(letter)
        counter[letter] -= 1
    return ''.join(stack)


# 132模式


S1 = 'CADB' # output: [(A, D, B)]
S2 = 'AEDB' # output: [(A, E, D), (A, D, B)]
S3 = 'ABADAD' # output: [ABA, ADA, DAD]


def _get_pre_table(S):
    N = len(S)
    pre_table = [[0 for _ in range(N+1)] for _ in range(26)]
    for i in range(26):
        for j in range(1, N):
            pre_table[i][j-1]
            count = 0
            for k in range(j+1, N):
                if ord(S[k]) > i + ord('A'):
                    count += 1
            pre_table[i][j] = count
    return pre_table

def _get_letter_list(S):
    N = len(S)
    letter_list = [[] for _ in range(26)]
    for i, letter in enumerate(S):
        letter_list[ord(letter) - ord('A')].append(i)
    return letter_list


def get_all_121_patterns(S):
    N = len(S)
    # A-0 B-1 C-2 ... Z-25
    # pre_table[0][0] 到 pre_table[0][N-1]: pre_table[i][j]: 在第j个位置，大于i的所有字母总数
    # 时间复杂度：O(n^2)
    # 空间复杂度：O(n^2)
    pre_table = _get_pre_table(S) 
    letter_list = _get_letter_list(S)
    ans = set()
    for i, l in enumerate(letter_list):
        if len(l) == 0:
            continue
        letter = chr(i + ord('A'))
        for i in range(1, len(l)):
            j, k = l[i-1], l[i]
            
            ans.add()
    print(pre_table)

get_all_121_patterns(S2)



