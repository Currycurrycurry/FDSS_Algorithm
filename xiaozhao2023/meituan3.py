from collections import Counter
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


s = list(input())

def get_min_str():
    if s == s[::-1]:
        i = 0
        while i < len(s) and s[i] == 'a':
            i += 1
        s[i] = 'a'
        s[len(s) - i - 1] = 'a'
        return ''.join(s)
    n = len(s)
    c = n // 2
    if n % 2 == 1:
        left, right = c - 1, c + 1
    else:
        left, right = c - 1, c
    cnt = 0
    while left >= 0 and right < n:
        if s[left] != s[right]:
            cnt += 1
            if ord(s[left]) < ord(s[right]):
                s[right] = s[left]
            else:
                s[left] = s[right]
        left -= 1
        right += 1
    if cnt < 2 and n % 2 == 1:
        s[c] = 'a'

    return ''.join(s)

print(get_min_str())
    

        
        
