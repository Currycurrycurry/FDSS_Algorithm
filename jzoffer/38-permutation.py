def permutation1(s):
    if not s:
        return []
    ans = []
    s = list(s)
    def helper(x):
        if x == len(s) - 1:
            ans.append(''.join(s))
            return
        keeped = set()
        for i in range(x, len(s)):
            if s[i] in keeped:
                continue
            keeped.add(s[i])
            s[i], s[x] = s[x], s[i]
            helper(x+1)
            s[i], s[x] = s[x], s[i]
    helper(0)
    return 

def permutation2(s):
    pass