"""
所有数组/字符串排列相关的递归/dfs问题
60. 第k个排列
384. 打乱数组
"""

# 获得str所有排列组合（非重复）
def permutation(S):
    res = []
    used = [False] * len(S)
    def helper(state):
        if len(state) == len(S):
            res.append(state)
            return
        for i in range(len(S)):
            if not used[i]:
                used[i] = True
                helper(state + S[i])
                used[i] = False
    helper("")
    return res

# 获得数组所有排列组合(非重复)
def permutation(nums):
    res = []
    used = [False] * len(nums)
    def helper(state):
        if len(state) == len(nums):
            res.append(state)
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                state.append(nums[i])
                helper(state)
                used[i] = False
    helper([])
    return res

# 获得有重复排列组合
def permutation(nums):
    pass

# python自带
def permutation(S):
    from itertools import permutations
    result = []
    for i in permutations(S, len(S)):
        result.append(''.join(i))
    return result

# 获得第n个排列组合
