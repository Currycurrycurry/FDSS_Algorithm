class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer < right_pointer:
            sum_value = nums[left_pointer] + nums[right_pointer]
            if sum_value < target:
                left_pointer += 1
            elif sum_value > target:
                right_pointer -= 1
            else:
                return [nums[left_pointer], nums[right_pointer]] 


# 和为s的连续正数序列
## wa
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left_value = 1
        right_value =  target//2 + 1
        ans = []
        while left_value >= 1 and right_value <= target//2 + 1:
            sum_value = (right_value - left_value + 1) * (left_value + right_value) // 2
            if sum_value > target:
                right_value -= 1
            elif sum_value < target:
                left_value += 1
            else:
                ans.append([i for i in range(left_value, right_value+1)])
        return ans

## ac
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left_value = 1
        right_value =  2
        ans = []
        while left_value <= target//2:
            sum_value = (right_value - left_value + 1) * (left_value + right_value) // 2
            if sum_value > target:
                left_value += 1
            elif sum_value < target:
                right_value += 1
            else:
                ans.append([i for i in range(left_value, right_value+1)])
                right_value += 1
        return ans