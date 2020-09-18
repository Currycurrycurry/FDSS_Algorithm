class KMP:
    def __init__(self, pat):
        self.pat = pat
        M = len(self.pat)
        self.dp = [[0]*256 for _ in range(M)]
        self.dp[0][ord(self.pat[0])] = 1
        X = 0
        for j in range(1, M):
            for c in range(256):
                self.dp[j][c] = self.dp[X][c]
            self.dp[j][ord(self.pat[j])] = j + 1
            X = self.dp[X][ord(self.pat[j])]
    
    def search(self, txt):
        M = len(self.pat)
        N = len(txt)
        j = 0
        for i in range(N):
            j = self.dp[j][ord(txt[i])]
            if j == M:
                return i - M + 1
        return -1

kmp = KMP('ABABC')
print(kmp.search('ABABABABABABC'))






