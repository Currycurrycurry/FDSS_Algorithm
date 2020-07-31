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

