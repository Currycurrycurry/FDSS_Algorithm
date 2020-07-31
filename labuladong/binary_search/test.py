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
    

'''









