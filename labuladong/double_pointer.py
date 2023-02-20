from typing import List
#注：不全是简单题。。有的时候很难想，值得注意!

######### 【原地修改数组】#########
# 26. 删除有序数组中的重复项
# 83. 删除排序链表中的重复元素
# 27. 移除元素
# 283. 移动零
def removeDuplicates(nums) -> int:
    length = len(nums)
    if length < 2:
        return length
    i = 0
    for j in range(1, length):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

def removeElement(nums, val) -> int:
    first_p = 0
    second_p = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        nums[first_p] = nums[i]
        first_p += 1
    return first_p if first_p else 0

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1

def deleteDuplicates(head):
    if not head or not head.next:
        return head
    if head.val == head.next.val:
        head = deleteDuplicates(head.next)
    else:
        head.next = deleteDuplicates(head.next)
    return head
######### 【左右指针】#########
# 包括：二分查找、回文串、滑动窗口、两数之和、反转数组
# 167. 两数之和 II - 输入有序数组
# 344. 反转字符串
# 5. 最长回文子串
# 剑指 Offer 57. 和为s的两个数字
def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1
    while start < end:
        if (numbers[start] + numbers[end]) == target:
            return [start + 1, end + 1]
        elif (numbers[start] + numbers[end]) < target:
            start += 1
        else:
            end -= 1
    return [start + 1, end + 1]

def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

def longestPalindrome(s) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right] # Be careful!
    start = 0
    end = 0
    res = ''
    for i in range(len(s)):
        s1 = expand(i, i)
        s2 = expand(i, i+1)
        res = s1 if len(s1) > len(res) else res
        res = s2 if len(s2) > len(res) else res
    return res


def advantageCount(self, nums1, nums2):
    n = len(nums1)
    ans = [0] * n
    nums1.sort()
    ids = sorted(range(n), key=lambda i: nums2[i])
    left, right = 0, n - 1
    for x in nums1:
        if x > nums2[ids[left]]:
            ans[ids[left]] = x  # 用下等马比下等马
            left += 1
        else:
            ans[ids[right]] = x  # 用下等马比上等马
            right -= 1
    return ans

# 1764. 通过连接另一个数组的子数组得到一个数组
def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
    def check(group_index, i):
        j = 0
        group = groups[group_index]
        length = len(group)
        while j < length and i < nums_len:
            if group[j] != nums[i]:
                return False
            i += 1
            j += 1
        return j == length
            
    group_len = len(groups)
    nums_len = len(nums)
    cnt = 0
    i, j = 0, 0
    while i < nums_len and j < group_len:
        if check(j, i):
            i += len(groups[j])
            j += 1
            cnt += 1
        else:
            i += 1
    return cnt == group_len