# hjn总是在奇奇怪怪的地方犯蠢)
# 剑指 Offer 27. 二叉树的镜像
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def mirrorTree(root):
    if root == null:
        return null
    tmp = root.left
    root.left = mirrorTree(root.right)
    root.right = mirrorTree(tmp)
    return root

# 剑指 Offer 48. 最长不含重复字符的子字符串
def lengthOfLongestSubstring(s):
    n = len(s)
    if n <= 1: 
        return n
    i, j = 0, 0
    res = 0
    while j < n - 1:
        j += 1
        while s[j] in s[i:j]:
            i += 1
        res = max(res, j - i + 1)
    return res

# 微服务架构

# 分布式计算

# 贪心算法与动态规划

