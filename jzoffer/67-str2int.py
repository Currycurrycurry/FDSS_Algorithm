# 字符串变成数字
def str2int(s):
    is_positive = True
    if s[0] == '-':
        is_positive = False
        num = int(s[1:])
    elif s[0] == '+':
        num = int(s[1:])
    else:
        num = int(s)
    if not is_positive:
        return -num
    return num


        