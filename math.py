# 求整数x的平方根
# 二分法
def mySqrt(self, x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

# 牛顿迭代法：二阶最优化算法，将损失函数进行二阶展开，因此会涉及到二阶导对应的海森矩阵。它的更新速度很快，但计算复杂度较高，主要是要求解海森矩阵的逆。
# 不仅可以用来求解函数极值问题，还可以求解方程的根
def mySqrt(self, x: int) -> int:
    if x == 0:
        return 0
    # y = x^2 - C -> sqrt(C)
    # 求导 y' = 2x
    C, x0 = float(x), float(x)
    while True:
        xi = 0.5 * (x0 + C / x0) # y = 2 * x_0 (x - x_0) + x_0^2 - C
        if abs(x0 - xi) < 1e-7:
            break
        x0 = xi 
    return int(x0)

# 求浮点数的平方根
def binary_sqrt(n):
    epsilon = 1e-10         # quit flag
    start = 0
    end = n
    mid = start + (end - start) / 2
    diff = mid ** 2 - n
    while abs(diff) >= epsilon:
        # 值过大则尝试小的一半，否则就尝试大的一半，修改边界值即可
        if diff > 0:
            end = mid
        else:
            start = mid
        mid = start + (end - start) / 2
        diff = mid ** 2 - n
    return mid

def newton_sqrt(n):
    x_n = n / 2
    epsilon = 1e-10             # quit flag
    
    f_x = lambda a : a**2 - n   # f(x)=x^2 - a
    df_x = lambda a : 2*a       # derivative of f(x)
    x_next = lambda a : a - f_x(a) / df_x(a)
    
    while abs(x_n ** 2 - n) > epsilon:
        x_n = x_next(x_n)
    return x_n

def gradient_sqrt(n):
    x       = n / 2       # first try
    lr      = 0.01        # learning rate
    epsilon = 1e-10       # quit flag
    
    f_x     = lambda a : a**2
    df_dx   = lambda a : 2*a
    delta_y = lambda a : f_x(a) -n
    e_x     = lambda a : delta_y(a)**2 * 0.5     # funcon of loss
    de_dx   = lambda a : delta_y(a) * df_dx(a)   # derivative of loss
    delta_x = lambda a : de_dx(a) * lr
    
    count   = 0
    while abs(x**2 - n) > epsilon:
        count += 1
        x = x - delta_x(x)
    return x, count

for i in range(1, 10):
    print(f'sqrt({i}): {gradient_sqrt(i)}次')

# 数值的整数次方
def myPow(self, x: float, n: int) -> float:
    is_positive = True if n > 0 else False
    
    def cal_postive_pow(x, n):
        if n == 1:
            return x
        if n == 0:
            return 1
        result = cal_postive_pow(x, n//2)
        result *= result
        if n % 2 == 1:
            result *= x
        return result

    if is_positive:
        return cal_postive_pow(x, n)
    else:
        return 1 / cal_postive_pow(x, -n)