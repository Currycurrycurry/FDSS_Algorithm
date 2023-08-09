from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, N: int):
        
        def func(x):
            left, right = x[0], x[1]
            if left > right:
                return (1, left)      # 为了方便 leave，允许 left > right ，但是设为正数 1，使其排名靠后
            if left == 0:
                return (-right, left)
            elif right == N - 1:
                return (-(right - left), left)
            else:
                return (-(right - left >> 1), left)      # (right - left >> 1) 计算选的座位到左右两边的距离，加负号的原因是默认排序是小的排前面。
                                                         # 根据题意，如果距离相等，区间左端点小的排在前面，因此加入 left
        self.n = N
        self.sl = SortedList([(0, N - 1)], key = func)      # 初始的时候 0 到 N-1 都可以坐下
        self.l2r = {0: N - 1}
        self.r2l = {N - 1: 0}
                
    def seat(self) -> int: 
        left, right = self.sl.pop(0)     # 选中目前到左右两边的距离最大的区间，如果距离相等，选区间左端点最小的
        if left == 0:
            p = 0
        elif right == self.n - 1:
            p = right
        else:
            p = (right + left) // 2
        # 新增被 p 划分的区间
        self.sl.add((left, p - 1))
        self.sl.add((p + 1, right))
        self.l2r[left] = p - 1
        self.r2l[right] = p + 1
        self.r2l[p - 1] = left
        self.l2r[p + 1] = right
        
        return p 
                
    def leave(self, p: int) -> None:
        left = self.r2l[p - 1]       # p-1 是之前被 p 划分的左半区间的右端点
        right = self.l2r[p + 1]      # p+1 是之前被 p 划分的右半区间的左端点

        # 下面 3 行是合并之前被 p 划分的区间
        self.sl.add((left, right))
        self.l2r[left] = right
        self.r2l[right] = left

        # 下面是清除残留区间
        self.sl.remove((left, p - 1))
        self.sl.remove((p + 1, right))
        self.r2l.pop(p - 1)
        self.l2r.pop(p + 1)
