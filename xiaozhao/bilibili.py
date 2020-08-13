def flat(arr):
    '''
    arr = [[1, 2 , 3], 4, 5, 6]
    '''
    def helper(arr, res=[]):
        for a in arr:
            if isinstance(a, int):
                res.append(a)
            else:
                helper(a, res)
        return res
    return helper(arr)

arr = [[1, 2 , 3], 4, 5, 6]
# arr = [4, 5, 6, [1, 2, 3]]
print(flat(arr))

# #coding=utf-8
# # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys 
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

# #coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)

def Game24Points(arr):
    def solve(arr):
        def calculate(a, b):
            res = set()
            res.add(a-b)
            res.add(b-a)
            res.add(a+b)
            res.add(a*b)
            if a != 0:
                res.add(b/a)
            if b != 0:
                res.add(a/b)
            return res
        if len(arr) == 1:
            return arr[0] == 24
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    nums = []
                    for k in range(len(arr)):
                        if k != i and k != j:
                            nums.append(arr[k])
                    res = calculate(arr[i], arr[j])
                    for r in res:
                        nums.append(r)
                        if solve(nums):
                            return True
                        nums.pop(-1)
        return False  
    return solve(arr)            

print(Game24Points([7, 2, 1, 10]))


def IsValidExp(s):
    if len(s) == 0:
        return True
    stack = []
    for i in s:
        if i == '{' or i == '(' or i == '[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
                else:
                    return False
            if i == '}':
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return False
            if i == ']':
                if stack[-1] == '[':
                    stack.pop(-1)
                else:
                    return False
    return len(stack) == 0

print(IsValidExp('{[]}'))


def coinChange3(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if (i - coin) < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1

def GetCoinCount(N):
    # write code here
    coins = [1, 4, 16, 64]
    N = 1024 - N
    dp = [N + 1] * (N + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if (i - coin) < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[N]

print(GetCoinCount(200))