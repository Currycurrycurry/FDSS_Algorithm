class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A or len(A) <= 2:
            return 0
        res = 0
        for i in range(1, len(A) - 1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                left, right = i-1, i+1
                while left > 0:
                    if A[left] > A[left-1]:
                        left -= 1
                while right < len(A) - 1:
                    if A[right] > A[right+1]:
                        right += 1
                res = max(res, right - left + 1)
        return res

import re

def to_str(n):
    return '+' if n > 0 else ('0' if n == 0 else '-')

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        s = ''.join(to_str(A[i]-A[i-1]) for i in range(1, len(A)))
        return max(map(lambda m: 1+len(m.group()), re.finditer(r'\++\-+', s)), default=0)

    def longestMountain(self, A: List[int]) -> int:
        length = len(A)
        if not A or length <= 2:
            return 0
        left = [0 for _ in range(length)]
        right = [0 for _ in range(length)]
        for i in range(1, length):
            left[i] = left[i-1] + 1 if A[i] > A[i-1] else 0
        for i in range(length-2, -1, -1):
            right[i] = right[i+1] + 1 if A[i] > A[i+1] else 0
        res = 0
        for i in range(length):
            if left[i] > 0 and right[i] > 0:
                res = max(res, right[i] + left[i] + 1)
        return res


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                if right < n - 1 and A[right] > A[right + 1]:
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                else:
                    right += 1
            left = right
        return ans
