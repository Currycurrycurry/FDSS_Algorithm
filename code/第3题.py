# 3
# 20212226543 黄佳妮
########### input processing ############
# N = int(input())

########### core algorithm ############
def encodeNums(num=0):
    try:
        if not num or num == 0 or num < 0:
            return 0
        num = str(num)
        length = len(num)
        dp = [1,1] + [0] * len(num)
        num = "99" + num
        for i in range(2, len(num)):
            if( 10 <= int(num[i-1:i+1]) <= 26):
                dp[i] += dp[i-2]
            if(num[i] != '0'):
                dp[i] += dp[i-1]
        return dp[-1]
    except Exception:
        return 0
    
########### test case 1 ############
print(encodeNums(14))
########### test case 2 ############
print(encodeNums(223))
########### test case 3 ############
print(encodeNums(130))
########### test case 4 ############
print(encodeNums(118))
########### test case 5 ############
print(encodeNums(0))
print(encodeNums(10))
print(encodeNums(100))
print(encodeNums(1))
########### test case 6 ############
print(encodeNums())
########### test case 7 ############
print(encodeNums(-1))
########### test case 8 ############
print(encodeNums(1000000000000))
########### test case 9 ############
print(encodeNums(-1000000000000))
