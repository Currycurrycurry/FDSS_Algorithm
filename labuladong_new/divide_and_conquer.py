# 分治算法详解：运算优先级

# 经典分治算法：归并排序
# O(nlogn) O(nlogn) o(nlogn) O(n) stable complex
def mergeSort(arr):        
    if not arr:
        return []
    mid = len(arr) // 2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    while left and right:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res

#  241 为运算表达式设计优先级
# 给你输入一个算式，你可以给它随意加括号，请你穷举出所有可能的加括号方式，并计算出对应的结果。

# 关键点一：不考虑整体，而是聚焦每个运算符
# 先想：如果不让括号嵌套（即只加一层括号），有几种加括号的方式？
# 回答：其实就是按照运算符进行分割，给【每个运算符的左右两部分】加括号

# 关键点二：明确函数的定义，相信并且利用这个函数的定义
# 也就是递归的作用

# 核心逻辑：扫描输入的算式input，每当遇到运算符就进行分割，递归计算出结果后，根据运算符来合并结果。
# 典型的分治思路，先「分」后「治」，先按照运算符将原问题拆解成多个子问题，然后通过子问题的结果来合成原问题的结果。

def diffWaysToCompute(expression: str):
    res = []
    for i, letter in enumerate(expression):
        if letter == '*' or letter == '-' or letter == '+':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for a in left:
                for b in right:
                    if letter == '*':
                        res.append(a * b)
                    elif letter == '-':
                        res.append(a - b)
                    elif letter == '+':
                        res.append(a + b)
    if len(res) == 0:
        res.append(int(expression))
    return res 

# 小优化：可以进行备忘录递归剪枝，减少一些重复计算
# (1 + 1) + (1 + 1 + 1)
# (1 + 1 + 1) + (1 + 1)
memo = dict() # memo
def diffWaysToCompute(expression: str):
    res = []
    if expression in memo:
        return memo[expression] # 避免重复计算
    for i, letter in enumerate(expression):
        if letter == '*' or letter == '-' or letter == '+':
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for a in left:
                for b in right:
                    if letter == '*':
                        res.append(a * b)
                    elif letter == '-':
                        res.append(a - b)
                    elif letter == '+':
                        res.append(a + b)
    if len(res) == 0:
        res.append(int(expression)) 
    memo[expression] = res # 将结果添加进备忘录
    return res 
