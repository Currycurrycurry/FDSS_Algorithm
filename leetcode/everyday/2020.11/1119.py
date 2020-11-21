class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return nums
        zero_index = nums.index(0)
        nonzero_index = zero_index
        while nonzero_index < len(nums) and nums[nonzero_index] == 0:
            nonzero_index += 1
        while nonzero_index < len(nums):
            nums[zero_index], nums[nonzero_index] = nums[nonzero_index], nums[zero_index]
            zero_index += 1
            while zero_index < len(nums) and nums[zero_index] != 0:
                zero_index += 1
            while nonzero_index < len(nums) and nums[nonzero_index] == 0:
                nonzero_index += 1
    
    def moveZeros(self, nums):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        while j < len(nums):
            nums[j] = 0
            