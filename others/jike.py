# Day1
# 删除排序数组中的重复项
# 双指针法
def removeDuplicates(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums_len
    i = 0
    for j in range(1, nums_len):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

test_nums = [0, 0, 1, 1, 2]
print(removeDuplicates(test_nums))
print(test_nums)

# 盛最多水的容器
def maxArea(height):
    max_value = 0
    left, right = 0, len(height) - 1
    while left < right:
        max_value = max(max_value, (right - left) * min(height[right], height[left]))
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return max_value

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# Day2
# N叉树的前序遍历
class NTreeNode:
    def __init__(self,val):
        self.children = []
        self.val = val

def preorder(root):
    if root:
        print(root.val)
        for child in root.children:
            preorder(child)

# 2叉树的前序遍历
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Day3
# 二叉树的最大深度
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)



# 验证二叉搜索树
def verifyBST(root):
    def recurse(root, lower, upper):
        if not root:
            return True

        val = root.val
        if lower and val <= lower:
            return False
        if upper and val >= upper:
            return False
        
        if not recurse(root.right, val, upper):
            return False
        if not recurse(root.left, lower, val):
            return False
        return True
    return recurse(root, None, None)

nodes = [TreeNode(i) for i in range(5)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]

print(maxDepth(nodes[0]))
print(preorder(nodes[0]))
print(verifyBST(nodes[0]))


# Day4 学习总结、
# 算法思路模板全整理 详见summary.md

# Day5 ~ Day7
def test():
    return None

import math
def test():
    print("hello world")
    return None

def test_2():
    if True:

    



