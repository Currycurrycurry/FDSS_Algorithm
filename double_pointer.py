from typing import List
#注：不全是简单题。。有的时候很难想，值得注意!
# <双指针技巧秒杀七道数组题目>

######### 【快慢指针：原地修改数组】#########
# 我们让慢指针 slow 走在后面，快指针 fast 走在前面探路，找到一个不重复的元素就赋值给 slow 并让 slow 前进一步。
# 这样，就保证了 nums[0..slow] 都是无重复的元素，当 fast 指针遍历完整个数组 nums 后，nums[0..slow] 就是整个数组去重之后的结果。
# 26. 删除有序数组中的重复项
# 83. 删除排序链表中的重复元素
# 27. 移除元素
# 283. 移动零

# 26. 删除有序数组中的重复项
def removeDuplicates(nums) -> int:
    length = len(nums)
    if length < 2:
        return length
    i = 0 # 慢指针i
    # 快指针j 复杂遍历
    for j in range(1, length):
        if nums[i] != nums[j]:
            # 找到不同的元素
            i += 1
            # 维护nums[0:i+1]无重复
            nums[i] = nums[j]
    return i + 1 # 数组长度为索引+1

# 27. 移除元素
def removeElement(nums, val) -> int:
    first_p = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        nums[first_p] = nums[i]
        first_p += 1
    return first_p if first_p else 0

# 283. 移动零
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

# 83. 删除排序链表中的重复元素
## 法一：递归
def deleteDuplicates(head):
    if not head or not head.next:
        return head
    if head.val == head.next.val:
        head = deleteDuplicates(head.next)
    else:
        head.next = deleteDuplicates(head.next)
    return head

## 法二：双指针迭代
# 像 Java/Python 这类带有垃圾回收的语言，可以帮我们自动找到并回收这些「悬空」的链表节点的内存.
# 而像 C++ 这类语言没有自动垃圾回收的机制，确实需要我们编写代码时手动释放掉这些节点的内存。
def deleteDuplicates(head):
    if not head or not head.next:
        return head
    slow, fast = head, head
    while fast:
        if fast.val != slow.val:
            # nums[slow] = nums[fast]
            slow.next = fast
            # slow += 1
            slow = slow.next
        fast = fast.next
    # 断开与后面重复元素的连接
    slow.next = None
    return head


######### 【左右指针】#########
# 包括：二分查找binary search、回文串、滑动窗口、两数之和、反转数组
# 167. 两数之和 II - 输入有序数组
# 344. 反转字符串
# 5. 最长回文子串
# 剑指 Offer 57. 和为s的两个数字

# 167. 两数之和 II - 输入有序数组
# 只要数组有序，就应该想到双指针技巧。
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

# 344. 反转字符串
def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

# 5. 最长回文子串
# 判断一个字符串是否是回文串容易，但找到一个字符串的最长回文串还是有难度的。
# 核心：从中心向两端扩散的双指针技巧
def longestPalindrome(s) -> str:
    # expand子函数：在s中寻找以s[left]和s[right]为中心的最长回文串
    def expand(left, right):
        # 防止索引越界
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 双指针向两边展开
            left -= 1
            right += 1
        return s[left+1:right] # Be careful!
    start = 0
    end = 0
    res = ''
    for i in range(len(s)):
        s1 = expand(i, i) # 寻找长度为奇数的字符串：以s[i]为中心的最长回文子串
        s2 = expand(i, i+1) # 寻找长度为偶数的回文串：以s[i]和s[i+1]为中心的最长回文子串
        # s1 s2两者取其大
        res = s1 if len(s1) > len(res) else res
        res = s2 if len(s2) > len(res) else res
    return res

# 田忌赛马
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