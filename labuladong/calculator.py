from collections import deque

# 不带括号的计算器
# 227. 基本计算器 II
def calculate(self, s: str) -> int: 
    s = deque(s)
    stack = []
    sign = '+'
    num = 0
    while len(s) > 0:
        c = s.popleft()
        if c.isdigit():
            num = 10 * num + int(c)

        if (not c.isdigit() and c != ' ') or len(s) == 0:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                # python 除法向 0 取整的写法
                stack[-1] = int(stack[-1] / float(num))                    
            num = 0
            sign = c
    return sum(stack)


# 224. 基本计算器：带加减乘除括号空格的计算器（hard）
def calculate(s):
    def helper(s):
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0:
            c = s.popleft()
            if c.isdigit():
                num = 10 * num + int(c)
            if c == '(':
                num = helper(s)
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / float(num))
                else:
                    pass
                num = 0
                sign = c
            if c == ')':
                break
        return sum(stack)
    return helper(deque(list(s)))

