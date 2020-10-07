class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, currIdx = 0, len(nums) - 1, 0
        while currIdx <= right:
            if nums[currIdx] == 0:
                nums[currIdx], nums[left] = nums[left], nums[currIdx]
                left += 1
                currIdx += 1
            elif nums[currIdx] == 2:
                nums[currIdx], nums[right] = nums[right], nums[currIdx]
                right -= 1
            else:
                currIdx += 1