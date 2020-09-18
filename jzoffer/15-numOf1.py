# 【错误解法】负数导致的死循环问题：右移导致最高位会设为1

def numOf1(n):
    flag = 1
    num_of_1 = 0
    while n:
        if flag & n == 1:
            num_of_1 += 1
        n >= 1
    return num_of_1

# 【正确解法】 左移flag
def numOf1_2(n):
    flag = 1
    num_of_1 = 0
    while flag < pow(2, 32):
        if flag & n == 1:
            num_of_1 += 1
        flag <= 1
    return num_of_1

# 【正确解法】 把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0。
def numOf1_3(n):
    cnt = 0;
    while n:
        cnt += 1
        n = (n - 1) & n
    return cnt

''' 判断二进制数中1的数目 【引申为】
（1） 判断一个整数是不是2的整数次方
（2） 输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n（先异或再统计1的个数）
'''


