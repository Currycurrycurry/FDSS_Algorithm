# hjn总是在奇奇怪怪的地方犯蠢)
# 剑指 Offer 27. 二叉树的镜像
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def mirrorTree(root):
    if root == null:
        return null
    tmp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(tmp)
    return root

# 剑指 Offer 48. 最长不含重复字符的子字符串
def lengthOfLongestSubstring(s):
    n = len(s)
    if n <= 1: 
        return n
    i, j = 0, 0
    res = 0
    while j < n - 1:
        j += 1
        while s[j] in s[i:j]:
            i += 1
        res = max(res, j - i + 1)
    return res

# 微服务架构

# 分布式计算

# 贪心算法与动态规划

# def getMembers(M, N):
#     matrix = [[0] * N for _ in range(M)]
#     res = []
#     cnt = 1
#     for i in range(min(M, N) - 1):
#         for r in range(i, N - i):
#             matrix[i][r] = cnt
#             if cnt >= 10 and cnt % 10 == 7 and ((cnt//10)%10)%2 == 1:
#                 res.append([i, r])
#             cnt += 1
#         for c in range(i+1, M - i):
#             matrix[c][N - i - 1] = cnt
#             if cnt >= 10 and cnt % 10 == 7 and ((cnt//10)%10)%2 == 1:
#                 res.append([i, r])
#             cnt += 1
#         for r in range(N - i - 2, i-1, -1):
#             matrix[M - 1 - i][r] = cnt
#             if cnt >= 10 and cnt % 10 == 7 and ((cnt//10)%10)%2 == 1:
#                 res.append([i, r])
#             cnt += 1
#         for c in range(M - i - 2, i - 1, -1):
#             if cnt >= 10 and cnt % 10 == 7 and ((cnt//10)%10)%2 == 1:
#                 res.append([i, r])
#             matrix[c][i] = cnt
#             cnt += 1
#     return res

def getMembers(M, N):
    matrix = [[0] * N for _ in range(M)]
    res = []
    cnt = 1
    start = 0
    def print_circle(matrix, start, rows, cols):
        row = rows - start - 1  # 最后一行
        col = cols - start - 1
        def checkIsMember(cnt):
            return cnt >= 10 and cnt % 10 == 7 and ((cnt//10)%10)%2 == 1
        # left->right
        nonlocal cnt
        for c in range(start, col+1):
            matrix[start][c] = cnt
            if checkIsMember(cnt):
                res.append([start, c])
            cnt += 1
        # top->bottom
        if start < row:
            for r in range(start+1, row+1):
                matrix[r][col] = cnt
                if checkIsMember(cnt):
                    res.append([r, col])
                cnt += 1
        # right->left
        if start < row and start < col:
            for c in range(start, col)[::-1]:
                matrix[row][c] = cnt
                if checkIsMember(cnt):
                    res.append([row, c])
                cnt += 1
        # bottom->top
        if start < row and start < col:
            for r in range(start+1, row)[::-1]:
                matrix[r][start] = cnt
                if checkIsMember(cnt):
                    res.append([r, start])
                cnt += 1
    while start * 2 < M and start * 2 < N:
        print_circle(matrix, start, M, N)
        start += 1
    return res
    
try:
    M, N = list(map(int, input().split(' ')))
    if M >= 10 and M <= 1000 and N >= 10 and N <= 1000:
        ans = getMembers(M, N)
        res = '['
        for i in range(len(ans)):
            res += ('[' + str(ans[i][0]) + ',' + str(ans[i][1]) + '],')
        res = res[:-1]
        res += ']'
        print(res)
    else:
        print([])
except Exception:
    print([])

# from itertools import combinations
# N = int(input())
# ds = list(map(int, input().split(' ')))
# def getTreeNumber(ds):
#     def getCnt(nums, num):
#         cnt = 0
#         for i in range(len(nums)):
#             if num == nums[i]:
#                 while num == nums[i] and i <len(nums):
#                     cnt += 1
#                     i += 1
#                 return cnt
#         return cnt
#     def getCnt(nums, num):
#         cnt = 0
#         for n in nums:
#             if n == num:
#                 cnt += 1
#         return cnt
#     res = 1
#     ds = sorted(ds)
#     ds_set = set(ds)
#     for value in ds_set:
#         cnt = getCnt(ds, value)
#         if cnt <= 0 or cnt > pow(2, value):
#             return 0
#         elif value - 1 >= 0 and cnt > getCnt(ds, value - 1) * 2:
#             print(value - 1)
#             print(getCnt(ds, value - 1))
#             return 0
#         elif value - 1 >= 0 and cnt < getCnt(ds, value - 1) * 2:
#             res *= len(list(combinations([i for i in range(getCnt(ds, value - 1)*2)], cnt)))
#     return res
# print(getTreeNumber(ds))