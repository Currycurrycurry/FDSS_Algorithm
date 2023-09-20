# KMP：（Knuth-Morris-Pratt 算法）
# 确定有限状态自动机
# KMP 算法永不回退txt的指针i，不走回头路（不会重复扫描txt）。
# 而是借助dp 数组中储存的信息把 pat 移到正确的位置继续匹配。
# 时间复杂度只需 O(N)，用空间换时间，所以我认为它是一种动态规划算法。
# 计算这个 dp 数组，只和 pat 串有关。

class KMP:
    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        self.dp = [[0 for _ in range(256)] for _ in range(M)]
        self.dp[0][ord(self.pat[0])] = 1
        # 影子状态X初始化为0
        X = 0
        for j in range(1, M):
            for c in range(0, 256):
                self.dp[j][c] = self.dp[X][c]
            self.dp[j][ord(self.pat[j])] = j + 1
            # 更新影子状态
            X = self.dp[X][ord(self.pat[j])]
    
    def search(self, txt):
        M = len(self.pat)
        N = len(txt)
        j = 0
        for i in range(0, N):
            j = self.dp[j][ord(txt[i])]
            if j == M:
                return i - M + 1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        kmp = KMP(needle)
        return kmp.search(haystack)