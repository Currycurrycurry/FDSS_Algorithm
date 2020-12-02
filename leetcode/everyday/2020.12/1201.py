class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]
        first_index = nums.index(target)
        second_index = len(nums) - nums[::-1].index(target) - 1
        return [first_index, second_index]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
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
        first_index, second_index = bs(
            nums, target, True), bs(nums, target, False) - 1
        # print(first_index)
        # print(second_index)
        if first_index <= second_index and second_index < len(nums) and nums[first_index] == target and nums[second_index] == target:
            return [first_index, second_index]
        else:
            return [-1, -1]
