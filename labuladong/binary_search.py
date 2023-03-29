from collections import defaultdict
import bisect 
# 二分查找本身不难理解，难在巧妙地运用二分查找技巧。
# 对于一个问题，你可能都很难想到它跟二分查找有关
# 牢记：「搜索区间」的概念，将搜索区间统一成两端都闭反而更加容易记忆
# find the target number
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

# left < right left == right [left, right] [left, right)
# left <= right [right + 1, right] [left, right]

# 补丁版
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return left if nums[left] == target else -1

# 局限性：无法在对数级复杂度中得到一个target的左侧边界或者右侧边界

def left_bound(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) # !

    while left < right: # !
        mid = (left + right) // 2
        # !关键：找到target后没有立即返回，而是缩小搜索区间的上界right，在区间[left, mid）中继续搜索
        # 不断向左收缩，达到锁定左侧边界的目的。
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid # !
    
    # 若不存在target这个值，则返回-1
    if left == len(nums):
        return -1
    return left if nums[left] == target else -1
    # ！返回left和right相同，因为while终止的条件是left == right

def left_bound2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 寻找右侧边界的二分查找
def right_bound(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        
    if left == 0:
        return -1
    return left - 1 if nums[left - 1] == target else -1

def right_bound2(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid + 1
        
    if right < 0 or nums[right] != target:
        return -1

    return right

'''
(1) 最基本的二分查找算法
    right = nums.length - 1
    决定了搜索区间是[left, right]
    决定了 while (left <= right)
    决定了 left = mid + 1
    决定了 right = mid - 1  

    只需要找到一个target的索引即可
    当nums[mid] == target时可以立即返回

（2）寻找左侧边界的二分查找
    

# 34. 在排序数组中查找元素的第一个和最后一个位置
'''
def searchRange(nums, target: int):
    def bs(nums, target, lower):
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1  
                ans = mid
            else:
                left = mid + 1
        return ans
    first_index, second_index = bs(nums, target, True), bs(nums, target, False) - 1
    # print(first_index)
    # print(second_index)
    if first_index <= second_index and second_index < len(nums) and nums[first_index] == target and nums[second_index] == target:
        return [first_index, second_index]
    else:
        return [-1, -1]


# 875. 爱吃香蕉的珂珂
from bisect import bisect_left
def minEatingSpeed(self, piles, h: int) -> int:
    # 3 6 7 11 Time: 8(H)
    # min_K
    # (0) 如果时间h<堆数len(piles) 肯定吃不完 -> h >=len(piles)
    #  h ==len(piles)-> max(piles)
    # (1) min：27 / 8 = 3 mod 3 -> K >= 4
    # (2) max：K<=max(piles)=11
    # K range: [4, 11]
    # 4, 5, 6, [7], 8, 9, 10, 11：1 + 1 + 1 + 2 = 5<H x 往左区间找 right=mid-1
    # 4, [5], 6, 7, 8, 9, 10, 11：1 + 2 + 2 + 3 = 8=H ok 往左区间找 right=mid-1
    # [4], 5, 6, 7, 8, 9, 10, 11：1 + 2 + 2 + 3 = 8 ok left==right==-1 
    # K range: [88/5, 30] = [18, 30]
    # mid=24: 2+1+1+1+1=6>H 往右区间找
    # mid=27: 2 + 1*4 = 6>H 往右区间找
    # mid=29: 2 + 1*4 = 6>H 往右区间找
    # mid=30: 5
    piles_len = len(piles)
    max_pile = max(piles)
    if h == piles_len:
        return max_pile
    pile_sum = sum(piles)
    # min_banana = pile_sum // piles_len
    # max_banana = max_pile
    return bisect_left(range(max_pile), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))

# 1011. 在 D 天内送达包裹的能力
def shipWithinDays(self, weights, days: int) -> int:
    # min: sum(weights) // days = 11
    # max: sum(weights) // 1 = 55
    lo, hi = max(weights), sum(weights)
    while(lo < hi):
        mid = (lo + hi) // 2 # mid 即为当前运送的capacity
        
        #------以下为模拟运货的过程，temp表示当天这条船承载的重量，day表示已用的天数-------
        temp = 0
        day = 1
        for weight in weights:
            temp += weight
            if temp > mid:# 当前货运不动 需要新的一艘船才行
                day += 1
                temp = weight
        #------以上为模拟运货的过程-----------------
        
        if day > days: # 当前的capacity太小了，不够，需要更大容量才能及时运完
            lo = mid + 1
        elif day <= days:
            hi = mid
    return lo

# 410. 分割数组的最大值
# 和上面这道在 D 天内送达包裹的能力的题如出一辙一模一样，换汤不换药。
def splitArray(self, nums, k: int) -> int:
    lo, hi = max(nums), sum(nums)
    while(lo < hi):
        mid = (lo + hi) // 2 # mid 即为当前的数组和
        temp = 0
        array_num = 1
        for num in nums:
            temp += num
            if temp > mid:# 当前子数组运不动 需要新的一个数组和才行
                array_num += 1
                temp = num 
        if array_num > k: # 当前的最大数组和太小了，不够，需要更大容量才能及时运完
            lo = mid + 1
        elif array_num <= k:
            hi = mid
    return lo



# 392. 判断子序列
def isSubsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    s_len = len(s)
    t_len = len(t)
    if s_len == 0:
        return True
    if t_len == 0:
        return False
    res = 0
    while i < t_len:
        if j < s_len:
            if s[j] == t[i]:
                res += 1
                j += 1
        i += 1
    return res == s_len


def isSubsequence(self, s: str, t: str) -> bool:
    def get_preprocessed_t(t):
        t_map = defaultdict(list)
        for index, letter in enumerate(t):
            t_map[letter].append(index)
        return t_map
    t_map = get_preprocessed_t(t)
    res = -1
    for i, letter in enumerate(s):
        if letter not in t_map.keys():
            return False
        pos_list = t_map[letter]
        target = bisect.bisect_right(pos_list, res)
        print(res)
        print(pos_list)
        print(target)
        if target >= len(pos_list) or pos_list[target] <= res:
            return False
        res = pos_list[target]
    return True
