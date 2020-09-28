''' 输入字符串的长度n还有一个只含有E和F两个字母的字符串
    输出所有子串里面E和F数量差值最大的值.
'''
def getMaxInterval(s):
    delta = 0
    deltas = []
    for i in s:
        if i == 'E':
            delta += 1
        else:
            delta -= 1
        deltas.append(delta)
    min_val = min(deltas)
    return max((max(deltas) - min_val), abs(min_val - max(deltas)), abs(min_val), max(deltas))


print(getMaxInterval('EFEEEEEEFF')) # 6
print(getMaxInterval('EEEEEEFFFFFFF')) # 7
print(getMaxInterval('FFFFFFEEEEE')) # 6
print(getMaxInterval('FEEFEEEEFFEE')) # 5
print(getMaxInterval('FEEFEEEEFFEE')) # 5
        