class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        max_len = len(arr) if len(arr) % 2 == 1 else len(arr) - 1
        for i in range(1, max_len+1, 2):
            for j in range(len(arr)-i+1):
                res += sum(arr[j:j+i])
        return res 