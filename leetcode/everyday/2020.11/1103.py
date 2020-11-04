class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A or len(A) < 3:
            return False
        positive_flag = True
        start = 0
        end = len(A) - 1
        while start < end and positive_flag:
            if A[start] < A[start + 1]:
                start += 1
                continue
            else:
                positive_flag = False
                break
        if start == len(A) - 1 or start == 0:
            return False
        while start < end and not positive_flag:
            if A[start] > A[start + 1]:
                start += 1
                continue
            else:
                return False
        return start == len(A) - 1


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l, r = 0, len(A) - 1
        while l < r and A[l] < A[l+1]: l += 1
        while l < r and A[r] < A[r-1]: r -= 1
        return l == r and l != 0 and r != len(A) - 1