######################## 对于括号合法性的判断，主要是借助「栈」这种数据结构

# ()括号匹配
def is_valid(str):
    # 待匹配的左括号数量
    left = 0
    for i in range(len(str)):
        if str[i] == '(':
            left += 1
        else:
            # 遇到右括号
            left -= 1
        # 右括号太多
        if left == -1:
            return False
    # 是否所有的左括号都被匹配了
    return left == 0

# （){}[]括号匹配
def isValid(s: str) -> bool:
    left = [] # 存放左括号
    for c in s:
        if c == '(' or c == '{' or c == '[': # 判断是否为左括号
            left.append(c) # 是左括号则加入列表
        else: # 是右括号
            if left and leftOf(c) == left[-1]: # 判断是否与最近的左括号匹配
                left.pop() # 匹配则将最近的左括号弹出
            else:
                return False # 不匹配则直接返回 false
    return not left # 是否所有的左括号都被匹配了

def leftOf(c: str) -> str:
    if c == '}': 
        return '{'
    elif c == ')':
        return '('
    else:
        return '['
    

def minAddToMakeValid(s: str) -> int:
    # res 记录插入次数
    res = 0
    # need 变量记录右括号的需求量
    need = 0

    for i in range(len(s)):
        if s[i] == '(':
            # 对右括号的需求 + 1
            need += 1
        elif s[i] == ')':
            # 对右括号的需求 - 1
            need -= 1
            if need == -1:
                need = 0
                # 需插入一个左括号
                res += 1
    
    return res + need

# 1541 平衡括号字符串的最少插入次数
def minInsertions(s: str) -> int:
    # 需要记录需右括号的需求量
    res = 0
    need = 0
    
    for i in range(len(s)):
        # 一个左括号对应两个右括号
        if s[i] == '(':
            need += 2
        
        if s[i] == ')':
            need -= 1
    
    return res + need


# 1541 题「平衡括号字符串的最少插入次数」：
# 现在假设 1 个左括号需要匹配 2 个右括号才叫做有效的括号组合，那么给你输入一个括号串 s，请问你如何计算使得 s 有效的最小插入次数呢？
def minInsertions(s: str) -> int:
    res, need = 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            need += 2
            if need % 2 == 1:
                res += 1
                need -= 1
        elif s[i] == ')':
            need -= 1
            if need == -1:
                res += 1
                need = 1
    return res + need

######################## 对于括号的生成，一般都要利用回溯递归的思想。

# 22. 括号生成
from typing import List

def generateParenthesis(n: int) -> List[str]:
    if n == 0: 
        return []
    # 记录所有合法的括号组合
    res = []
    # 回溯过程中的路径
    track = ''
    # 可用的左括号和右括号数量初始化为 n
    backtrack(n, n, track, res)
    return res

# 可用的左括号数量为 left 个，可用的右括号数量为 rgiht 个
def backtrack(left: int, right: int, track: str, res: List[str]) -> None:
    # 若左括号剩下的多，说明不合法
    if right < left:
        return
    # 数量小于 0 肯定是不合法的
    if left < 0 or right < 0:
        return
    # 当所有括号都恰好用完时，得到一个合法的括号组合
    if left == 0 and right == 0:
        res.append(track)
        return
    
    # 尝试放一个左括号
    track += '(' # 选择
    backtrack(left - 1, right, track, res)
    track = track[:-1] # 撤消选择

    # 尝试放一个右括号
    track += ')' # 选择
    backtrack(left, right - 1, track, res)
    track = track[:-1] # 撤消选择

# 解数独
def backtrack(board: List[List[str]], i: int, j: int) -> bool:
    m, n = 9, 9
    if j == n:
        # 穷举到最后一列的话就换到下一行重新开始。
        return backtrack(board, i + 1, 0)
    if i == m:
        # 找到一个可行解，触发 base case
        return True

    if board[i][j] != '.':
        # 如果有预设数字，不用我们穷举
        return backtrack(board, i, j + 1)

    for ch in range(ord('1'), ord('9') + 1):
        ch = chr(ch)
        # 如果遇到不合法的数字，就跳过
        if not isValid(board, i, j, ch):
            continue
        
        board[i][j] = ch
        # 如果找到一个可行解，立即结束
        if backtrack(board, i, j + 1):
            return True
        board[i][j] = '.'
    # 穷举完 1~9，依然没有找到可行解，此路不通
    return False

# 判断 board[i][j] 是否可以填入 n
def isValid(board: List[List[str]], r: int, c: int, n: str) -> bool:
    for i in range(9):
        if board[r][i] == n:
            return False
        if board[i][c] == n:
            return False
        if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
            return False
    return True

# 241. 为运算表达式设计优先级
class Solution:
    def __init__(self):
        self.memo = {}

    def diffWaysToCompute(self, input: str) -> List[int]:
        # 避免重复计算
        if input in self.memo:
            return self.memo[input]
        res = []
        for i in range(len(input)):
            c = input[i]
            # 扫描算式 input 中的运算符
            if c in ['-', '*', '+']:
                # 以运算符为中心，分割成两个字符串，分别递归计算
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 通过子问题的结果，合成原问题的结果
                for a in left:
                    for b in right:
                        if c == '+':
                            res.append(a + b)
                        elif c == '-':
                            res.append(a - b)
                        elif c == '*':
                            res.append(a * b)
        # base case
        # 如果 res 为空，说明算式是一个数字，没有运算符
        if not res:
            res.append(int(input))
        # 将结果添加进备忘录
        self.memo[input] = res
        return res