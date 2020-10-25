class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        
        return -1 if dp[T] == float("inf") else dp[T]