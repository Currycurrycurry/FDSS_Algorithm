'''
    字符串匹配算法合集
'''
# BF算法（Brute-Force算法）简单朴素的模式匹配算法，用于在一个主串S内查找一个子串T的出现位置。

def bf(t, s):
    if not t or not s:
        return False
    s_index, t_index = 0, 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
            t_index += 1
        else:
            s_index = (s_index - t_index + 1)
            t_index = 0
    if t_index == len(t):
        return True
    else:
        return False

# RK算法 Rabin & Karp
'''
RK算法是对BF算法的一个改进：
在BF算法中，每一个字符都需要进行比较，
并且当我们发现首字符匹配时仍然需要比较剩余的所有字符。
 而在RK算法中，就尝试只进行一次比较来判定两者是否相等。 RK算法也可以进行多模式匹配，在论文查重等实际应用中一般都是使用此算法。
''' 
def rk(t, s):
    pass



    
    










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






