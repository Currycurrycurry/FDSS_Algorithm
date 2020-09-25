li = [[1,2,3],[4,5,6],[7,8,9]]
li_T = [list(i) for i in zip(*li)]

print(li_T)

def zip_demo(list1, list2):
    li1 = iter(list1)
    li2 = iter(list2)
    try:
        while True:
            item1 = next(li1)
            item2 = next(li2)
            yield item1, item2
    except StopIteration:
        pass
li1 = [1,2,3]
li2 = ['a', 'b', 'c']
for i in zip_demo(li1, li2):
    print(i)


def transpose(A):
    col_len = len(A)
    if not A or col_len == 0:
        return []
    row_len = len(A[0])
    if row_len == 0:
        return [[]]
    res = []
    for i in range(row_len):
        tmp = []
        for j in range(col_len):
            tmp.append(A[j][i])
        res.append(tmp)
    return res