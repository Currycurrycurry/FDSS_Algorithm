class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        left_p, right_p = 0, len(A) - 1
        while left_p <= right_p:
            if abs(A[right_p]) >= abs(A[left_p]):
                res.append(A[right_p] * A[right_p])
                right_p -= 1
            else:
                res.append(A[left_p] * A[left_p])
                left_p += 1
        return res[::-1]