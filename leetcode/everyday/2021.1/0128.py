class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        length = len(nums)
        left_sum = [nums[0] for _ in range(length)]
        right_sum = [nums[-1] for _ in range(length)]
        for i in range(1, length):
            left_sum[i] = left_sum[i-1] + nums[i]
        for i in range(length - 2, -1, -1):
            right_sum[i] = right_sum[i+1] + nums[i]
        if right_sum[1] == 0:
            return 0
        for i in range(1, length-1):
            if left_sum[i-1] == right_sum[i+1]:
                return i
        if left_sum[-2] == 0:
            return length - 1
        return -1 

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_left = 0
        length = len(nums)
        for i in range(length):
            if sum_left * 2 + nums[i] == sum_nums:
                return i
            sum_left += nums[i]
        return -1