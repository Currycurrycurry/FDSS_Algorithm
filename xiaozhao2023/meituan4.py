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

N, X, Y = map(int, input().strip().split())
os = []
cs =[]
for i in range(N):
    o, c = list(map(int, input().strip().split()))
    os.append(o)
    cs.append(c)

def get_best():
    
    return str(res_num) + ' ' + str(res_cost)

    # dp[i][j] i items price j

print(get_best)