import copy

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # part1
        l, r = 0, len(A) - 1
        while l < r:
            while l < r and not (A[l]%2 == 0 and l%2 == 1):
                l += 1
            while l < r and not (A[r]%2 == 1 and r%2 == 0):
                r -= 1
            A[l], A[r] = A[r], A[l]
        
        l, r = 0, len(A) - 1
        while l < r:
            while l < r and not (A[l]%2 == 1 and l%2 == 0):
                l += 1
            while l < r and not (A[r]%2 == 0 and r%2 == 1):
                r -= 1
            A[l], A[r] = A[r], A[l]
        return A 
    
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = copy.deepcopy(A)
        i = 0
        for a in A:
            if a % 2 == 0:
                res[i] = a 
                i += 2
        i = 1
        for a in A:
            if a % 2 == 1:
                res[i] = a 
                i += 2
        return res

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 1
        for j in range(0, len(A), 2):
            if A[j] % 2 == 1:
                while A[i] % 2 == 1:
                    i += 2
                A[i], A[j] = A[j], A[i]
        return A