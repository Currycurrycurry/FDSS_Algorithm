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

N, K = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
 


def get_max_length():
    if N <= 1:
        return N
    i, j = 0, 0
    res = 0
    while j < N - 1:
        j += 1
        while len(set(nums[i:j])) > K:
            i += 1
        res  = max(res, j - i)
    return res


print(get_max_length())

