# 洗牌算法：靠随机选取元素交换来获取随机性
import random
def shuffle1(nums):
    n = len(nums)
    for i in range(n):
        rand = random.randint(i, n-1)
        nums[rand], nums[i] = nums[i], nums[rand]

def shuffle2(nums):
    n = len(nums)
    for i in range(n-1):
        rand = random.randint(i, n-1)
        nums[rand], nums[i] = nums[i], nums[rand]

def shuffle3(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        rand = random.randint(0, i)
        nums[rand], nums[i] = nums[i], nums[rand]

def shuffle4(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        rand = random.randint(0, i)
        nums[rand], nums[i] = nums[i], nums[rand]

# 概率均等


# 528. 按权重随机选择
# 二分搜索【左侧边界】模板
# 前缀和
import random
class Solution:
    def __init__(self, w):
        # w: [1, 3, 4, 6]
        # pre_sum: [0, 1, 4, 8, 14]
        # uniform random number from pre_sum array: [1, presum[-1]]
        # get the left index of the target random pre_sum (index need off one -1)
        self.pre_sum = [0 for _ in range(len(w) + 1)]
        for i in range(len(w)):
            self.pre_sum[i+1] = self.pre_sum[i] + w[i]
    
    def _left_bound(self, array, target):
        if len(array) == 0:
            return -1
        left, right = 0, len(array)
        while left < right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                right = mid
            elif array[mid] < target:
                left = mid + 1
            elif array[mid] > target:
                right = mid
        return left

    def pickIndex(self) -> int: 
        rand = random.randint(1, self.pre_sum[-1])
        index = self._left_bound(self.pre_sum, rand) - 1
        return index

# 380. O(1) 时间插入、删除和获取随机元素
import random
class RandomizedSet:

    def __init__(self):
        self.array = []
        self.value_to_index = dict()


    def insert(self, val: int) -> bool:
        if val in self.value_to_index.keys():
            return False
        index = len(self.array)
        self.array.append(val)
        self.value_to_index[val] = index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_index.keys():
            return False
        index = self.value_to_index[val]
        end_val = self.array[-1]
        self.value_to_index[end_val] = index
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.array.pop()
        self.value_to_index.pop(val)

        return True

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]

# 710. 黑名单中的随机数
import random
class Solution:

    def __init__(self, n: int, blacklist):
        self.num_len = n - len(blacklist)
        self.map = dict()
        for num in blacklist:
            self.map[num] = 666
        last = n - 1
        for num in blacklist:
            if num >= self.num_len:
                continue
            while last in self.map.keys():
                last -= 1
            self.map[num] = last
            last -= 1
        
    def pick(self) -> int:
        index = random.randint(0, self.num_len - 1)
        if index in self.map.keys():
            return self.map[index]
        return index