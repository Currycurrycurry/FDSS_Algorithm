n = int(input())
nums = list(map(int, input().split()))

def encode(num):
    ans = ''
    while num > 0:
        cur = num % 10
        tmp = bin(cur)[2:]
        for i in range(4 - len(tmp)):
            tmp = '0'+tmp
        # print('tmp is ' + tmp)
        ans = tmp + ans
        num = num // 10
    for i in range(12 - len(ans)):
        ans = '0' + ans
    # print(ans)
    ans = ans[::-1]
    start = 0
    while start < len(ans) and ans[start] == '0':
        start += 1
    return ans[start:]

for i in range(n):
    print(encode(nums[i]))
        
# nums = [i for i in range(999)]

# for i in range(999):
#     print('{i}: {ans}'.format(i=i, ans=encode(nums[i])))