'''
# get a number
n = int(input())

# get a list
nums = list(map(int, input().strip().split()))

# get 2/3/4 nums in a line
a, b, c, d = map(int, input().strip().split())

# get a matrix
row, col = map(int, input().strip().split())
matrix = []
for i in range(row):
    line = list(map(int, input().strip().split()))
    matrix.append(line)

print(n, nums, a, b, c, d, matrix)
'''

N, A, B = map(int, input().strip().split())
points = []
xs = []
ys = []
for i in range(N):
    point = list(map(int, input().strip().split()))
    xs.append(point[0])
    ys.append(point[1])
    points.append(point)

# 返回最长不超过某个A/B的连续数组
def get_sets(sorted_index, list, value):
    ans = {0}
    min_value = list[sorted_index[0]]
    for i in sorted_index[1:]:
        if list[sorted_index[i]] - min_value <= value:
            ans.add(i)
    return ans

    
def get_max_point():
    x_sorted = sorted(range(N), key = lambda x: xs[x])
    y_sorted = sorted(range(N), key = lambda y: ys[y])
    x_sets = [get_sets(x_sorted, xs, A)]
    # print(x_sets)
    y_sets = [get_sets(y_sorted, ys, B)]
    # print(y_sets)
    num = 1
    for x_set in x_sets:
        for y_set in y_sets:
            if len(x_set & y_set)  > num:
                num = len(x_set & y_set)
    return num
    
print(get_max_point())
