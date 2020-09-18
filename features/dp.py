class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s):
            ans = False
            if not s or len(s) == 0:
                return True
            for word in wordDict:
                if word == s[0:len(word)]:
                    ans = helper(s[len(word):])
                if ans:
                    return True
            return ans
        return helper(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for word in wordDict:
                if len(word) + i <= len(s) and s[i:len(word)+i] == word and dp[i]:
                    dp[len(word)+i] = True
        return dp[-1]
