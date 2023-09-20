from typing import List
'''
76. 最小覆盖子串
567. 字符串的排列
438. 找到字符串中所有字母异位词
3. 无重复字符的最长子串
'''
# 核心：设计滑动窗口区间【一定要左闭右开】：[left，right)

from collections import defaultdict

# 76. 最小覆盖子串
def minWindow(s: str, t: str) -> str:
    left, right = 0, 0 # [left, right)
    need = defaultdict(int)
    for letter in t:
        need[letter] += 1
    need_len = len(need.keys())
    valid = 0
    window = defaultdict(int)
    res_start = 0
    res_len = float('inf')
    while right < len(s):
        curr_letter = s[right]
        right += 1
        window[curr_letter] += 1
        if window[curr_letter] == need[curr_letter]:
            valid += 1
        
        while valid == need_len:
            if right - left < res_len:
                res_start = left
                res_len = right - left
            curr_letter = s[left]
            left += 1
            if curr_letter in need:
                if window[curr_letter] == need[curr_letter]:
                    valid -= 1
                window[curr_letter] -= 1

    return s[res_start:res_start + res_len] if res_len != float('inf') else ''

# 567. 字符串的排列
def checkInclusion(self, s1: str, s2: str) -> bool:
    left, right = 0, 0
    valid = 0
    need_dict = defaultdict(int)
    s1_len = len(s1)
    s2_len = len(s2)
    for letter in s1:
        need_dict[letter] += 1
    need_len = len(need_dict.keys())
    window = defaultdict(int)
    # print(need_dict)
    while right < s2_len:
        curr_letter = s2[right]
        right += 1
        if curr_letter in need_dict.keys():
            window[curr_letter] += 1
            if window[curr_letter] == need_dict[curr_letter]:
                valid += 1
        # print(window)
        
        while valid == need_len:
            if right - left == s1_len:
                return True
            curr_letter = s2[left]
            left += 1
            if curr_letter in need_dict.keys():
                if window[curr_letter] == need_dict[curr_letter]:
                    valid -= 1
                window[curr_letter] -= 1
    return False

# 438. 找到字符串中所有字母异位词
def findAnagrams(s: str, p: str):
    left, right = 0, 0
    need_dict = defaultdict(int)
    for letter in p:
        need_dict[letter] += 1
    need_len = len(need_dict.keys())
    p_len = len(p)
    s_len = len(s)
    window = defaultdict(int)
    valid = 0
    res = []
    while right < s_len:
        curr_letter = s[right]
        right += 1
        if curr_letter in need_dict.keys():
            window[curr_letter] += 1
            if window[curr_letter] == need_dict[curr_letter]:
                valid += 1
        while valid == need_len:
            if right - left == p_len:
                res.append(left)
    
            curr_letter = s[left]
            left += 1
            if curr_letter in need_dict.keys():
                if window[curr_letter] == need_dict[curr_letter]:
                    valid -=1
                window[curr_letter] -= 1
    return res

# 3. 无重复字符的最长子串
def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) <= 1:
        return len(s)
    left, right = 0, 0
    max_len = 0
    while right < len(s) - 1:
        right += 1
        while s[right] in s[left:right]:
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# 在滑动窗口中快速计算窗口中元素的哈希值，叫做滑动哈希技巧。

# 平均时间复杂度是 O(N)，极端情况下的时间复杂度会退化成 O(NL)。
# 187. 重复的DNA序列
def findRepeatedDnaSequences(self, s: str):
    DNA = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    nums = []
    for letter in s:
        nums.append(DNA[letter])
    LEN = 10 # 数字位数/数字长度
    TYPE_NUM = 4 # 进制
    MAX_NUM = TYPE_NUM ** (LEN - 1) # 最大四进制十位数是4^9
    window_hash = 0 # 滑动窗口的hash值
    seen = set()
    res = set()
    left, right = 0, 0
    # 核心逻辑
    while right < len(nums):
        window_hash = TYPE_NUM * window_hash + nums[right]
        print(window_hash)
        right += 1
        if right - left == LEN:
            if window_hash in seen:
                res.add(s[left:right])
            else:
                seen.add(window_hash)
            window_hash -= nums[left] * MAX_NUM
            left += 1
    return list(res)

# 28. 找出字符串中第一个匹配项的下标
# 【Rabin Karp算法】
# 时间复杂度是 O(N + L)，N 为文本串 txt 的长度，L 为模式串 pat 的长度。
# 当然，每次出现哈希冲突时会使用 O(L) 的时间进行暴力匹配，
# 但考虑到只要 Q 设置的合理，哈希冲突的出现概率会很小，所以可以忽略不计。
def strStr(haystack: str, needle: str) -> int:
    L = len(needle) # 位数
    R = 256 # ascii进制
    Q = 1658598167 # 【比较大】的【素数】（作为除数，可以【有效防止哈希碰撞】）
    RL = 1
    for i in range(1, L):
        RL = (RL * R) % Q
    
    needle_hash = 0
    for i in range(L):
        needle_hash = (R * needle_hash + ord(needle[i])) % Q
    print(needle_hash)
    
    window_hash = 0
    left, right = 0, 0
    while right < len(haystack):
        window_hash = ((R * window_hash) % Q + ord(haystack[right])) % Q
        print(window_hash)
        right += 1
        if right - left == L:
            if window_hash == needle_hash:
                print('!')
                if haystack[left:right] == needle:
                    return left
            # window_hash = (window_hash - (RL * ord(haystack[left])) % Q ) % Q
            window_hash = ((window_hash - (ord(haystack[left]) * RL) % Q) + Q) % Q
            left += 1
    return -1

# 1703. 得到连续 K 个 1 的最少相邻交换次数
## 难！非常难！但值得反复刷！
## 综合了贪心、滑动窗口、前缀和的思想，是一道非常好的题目！
# 第一次最少相邻交换次数：时间复杂度O(N*M) 空间复杂度O(N*M)
def minMoves(self, nums: List[int], k: int) -> int:
    # 获得窗口内从左往右的前缀和
    def get_left_presum(left, right):
        pass
    # 获得窗口内从右往左的前缀和
    def get_right_presum(left, right):
        pass
    def calculate_cost(left, right):
        # [left, right)
        left_presum = get_left_presum(left, right)
        right_presum = get_right_presum(left, right)
        total_cost = 0
        for i in range(left, right, 1):
            total_cost += min(left_presum[i], right_presum[i])
        return total_cost
    left, right = 0, k # [left, right)
    k_count = 0
    min_cost = float('inf')
    while right < len(nums):
        # enlarge the window 
        while right < len(nums) and k_count < k:
            if nums[right] == 1:
                k_count += 1
            right += 1
        while k_count == k:
            total_cost = calculate_cost(left, right)
            min_cost = min(min_cost, total_cost)
            if nums[left] == 1:
                k_count -= 1
            left += 1
    return min_cost

# 第二次最少相邻交换次数：时间复杂度O(N) 空间复杂度O(n)

# 1658. 将 x 减到 0 的最小操作数
# 转换思路，相当于求和等于sum(nums)-x的最长子数组的长度，
# 然后用len(nums)减去这个结果。由于元素均为正数，可以用滑动窗口解
def minOperations(self, nums: List[int], x: int) -> int:
    n = len(nums)
    res = -1
    sum_nums = sum(nums)
    target = sum_nums - x
    left = 0
    subsum = 0
    for right in range(n):
        subsum += nums[right]
        while left <= right and subsum > target:
            subsum -= nums[left]
            left += 1
        if subsum == target:
            res = max(res, right - left + 1)
    return n - res if res >= 0 else -1