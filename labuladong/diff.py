# 差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减。
# 回想 diff 数组反推 nums 数组的过程:
# diff[i] += 3 意味着给 nums[i..] 所有的元素都加了 3，
# 然后 diff[j+1] -= 3 又意味着对于 nums[j+1..] 所有元素再减 3，
# 那综合起来，是不是就是对 nums[i..j] 中的所有元素都加 3 了？
class Difference:
    def __init__(self, nums):
        self.diff = [0 for _ in range(len(nums))]
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    
    def result(self):
        res = [0 for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

# 370.区间加法
def getModifiedArray(length, updates):
    nums = [0 for _ in range(length)]
    diff = Difference(nums)
    for update in updates:
        i, j, val = update
        diff.increment(i, j, val)
    return diff.result()

# 1109. 航班预订统计
def corpFlightBookings(bookings, n: int):
    nums = [0 for _ in range(n)]
    diff = Difference(nums)
    for update in bookings:
        i, j, val = update[0] - 1, update[1] - 1, update[2]
        diff.increment(i, j, val)
    return diff.result()

# 1094. 拼车
def carPooling(self, trips, capacity) -> bool:
    nums = [0 for _ in range(1001)]
    diff = Difference(nums)
    for trip in trips:
        val, i, j = trip[0], trip[1], trip[2] - 1
        diff.increment(i, j, val)
    res = diff.result()
    for r in res:
        if r > capacity:
            return False
    return True