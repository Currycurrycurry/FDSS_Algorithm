class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]
        first_index = nums.index(target)
        second_index = len(nums) - nums[::-1].index(target) - 1
        return [first_index, second_index]
        


        