class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        res = N
        while True:
            nums = list(map(int, list(str(res))))
            flag = True
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    flag = False
                    break
            if flag:
                return res
            res -= 1


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = list(map(int, list(str(N))))
        i = 1
        while i < len(N) and N[i-1] <= N[i]:
            i += 1
        if i < len(N):
            while i > 0 and N[i] < N[i-1]:
                N[i - 1] -= 1
                i -= 1
            for j in range(i+1, len(N)):
                N[j] = 9
        return ''.join(list(map(str, N))).lstrip('0')


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        i = 1
        res = N
        while i <= res//10:
            n = res // i % 100
            i *= 10
            if n // 10 > n % 10:
                res = res // i * i - 1
        return res
