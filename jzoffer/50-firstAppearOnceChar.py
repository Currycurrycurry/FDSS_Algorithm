# python遍历dict的顺序是否是添加的顺序？
def getFirstAppearOnceChar(s):
    tmp = dict()
    for i in s:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] == 1
    for t in tmp.keys():
        if tmp[t] == 1:
            return t
    return -1






