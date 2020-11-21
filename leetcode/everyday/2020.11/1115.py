class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if length <= k:
            return '0'
        num = list(map(int, list(num)))
        while k > 0:
            if num[0] > num[1]:
                num.pop(0)
            else:
                i = 1
                while i < len(num) and num[i] >= num[i-1]:
                    i += 1
                num.pop(i-1)
            k -= 1
        i = 0
        while i < len(num) and num[i] == 0:
            i += 1
        if len(num[i:]) == 0:
            return '0'
        else:
            return ''.join(list(map(str, num[i:])))


            