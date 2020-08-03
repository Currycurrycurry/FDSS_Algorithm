n, k = list(map(int, input().split()))
def getAns(n, k):
    if k == n:
        ans = ''
        for i in range(n):
            ans += chr(ord('a') + i)
        return ans
    if k > n or k == 1:
        return -1
    first_part = ['a']
    for i in range(1, n - k + 2, 1):
        if first_part[i - 1] == 'a':
            first_part.append('b')
        else:
            first_part.append('a')
    first_part = ''.join(first_part)
    second_part = ''
    for i in range(k - 2, 0, -1):
        second_part += chr(ord('a') + k-i)
    return ''.join(first_part + second_part)

print(getAns(n, k))
    
    