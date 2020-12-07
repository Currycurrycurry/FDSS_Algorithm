class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] = 1 ^ A[i][j]
        sum = 0
        print(list(zip(*A)))
        for i in zip(*A):
            m -= 1
            sum += 2 ** m * max(i.count(1),i.count(0))
        return sum