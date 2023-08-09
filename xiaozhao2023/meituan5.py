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
N = int(input())
es = list(map(int, input().strip().split()))
edges = []
for i in range(N - 1):
    edge = list(map(int, input().strip().split()))
    edges.append(edge)

matrix = [[0 for _ in range(N)] for _ in range(N)]
for edge in edges:
    matrix[edge[0] - 1][edge[1] - 1] = 1
    matrix[edge[1] - 1][edge[0] - 1] = 1

res = [1 for _ in range(N)]

def dfs(node, e, root):
    if e == 0:
        return 0
    for i, v in enumerate(matrix[node]):
        if v == 1 and i != root:
            res[i] += 1
            dfs(i, e - 1, node)

for i in range(N):
    e = es[i]
    dfs(i, e, None)

print(' '.join(list(map(str, res))))









