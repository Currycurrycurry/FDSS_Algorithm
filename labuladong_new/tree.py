# 6
# RBRRBR
# 1 1 2 2 3
n = int(input())
colors = input()
nums = list(map(int, input().split(' ')))
cnt = 0
def helper(n):
    global cnt
    r = 0
    b = 0
    for i in range(n):
        if nums[i] == n:
            sr, sb = helper(i+1)
            r += sr
            b += sb
    if r == b:
        if colors[n-1] == 'R':
            r += 1
        else:
            b += 1
        if r == b:
            cnt += 1
    return r, b
helper(1)
print(cnt)
            