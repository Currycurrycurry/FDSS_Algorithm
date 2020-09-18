class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s: string
        # p: pattern string
        def helper(s_index, p_index):
            if s_index == len(s) and p_index == len(p):
                return True
            if s_index < len(s) and p_index >= len(p):
                return False
            if p_index < len(p) - 1 and s_index < len(s) and p[p_index + 1] == '*':
                if p[p_index] == s[s_index] or (p[p_index] == '.' and s_index < len(s)):
                    return helper(s_index + 1, p_index + 2) or \
                           helper(s_index + 1, p_index) or \
                           helper(s_index, p_index + 2)
                else:
                    return helper(s_index, p_index + 2)
            if s_index < len(s) and p_index < len(p):
                if s[s_index] ==p[p_index] or (p[p_index] == '.' and s_index < len(s)):
                    return helper(s_index + 1, p_index + 1)
            return False
            
        if not s or not p:
            return False
            
        return helper(0, 0)


        