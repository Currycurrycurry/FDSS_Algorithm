class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        s_len = len(s)
        p_len = len(p)
        def dp(i, j):
            if (i, j) in memo.keys():
                return memo[(i, j)]
            # base case 1: s和p都匹配完全
            if j == p_len:
                return i == s_len
            # base case 2: s匹配到底，p剩余的都是*和字母的合理（可以被消掉的）组合
            if i == s_len:
                if (p_len - j) % 2 != 0:
                    return False
                # 进一步判断剩余字符串是否是[字母*]的模式
                for k in range(j+1, p_len, 2):
                    if p[k] != '*':
                        return False
                return True
            # core function
            res = False
            # branch 1: 匹配
            if s[i] == p[j] or p[j] == '.':
                if j < p_len - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2) or dp(i + 1, j) # 匹配0次或多次
                else:
                    res =  dp(i + 1, j + 1) # 匹配一次
            # branch 2: 不匹配
            else:
                if j < p_len - 1 and p[j + 1] == '*':
                    res = dp(i, j + 2) # 匹配0次
                else:
                    res = False # 无法匹配
            memo[(i, j)] = res
            return res
        return dp(0, 0)


        