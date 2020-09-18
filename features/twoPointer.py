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

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) <= 2:
            return 0
        # find max
        max_index = 0
        max_value = height[0]
        for i in range(len(height)):
            if height[i] > max_value:
                max_index = i
                max_value = height[i]
        area = 0
        # from left to max
        left_max = 0
        for i in range(1, max_index):
            if height[i] > height[left_max]:
                left_max = i
            else:
                area += (height[left_max] - height[i])
        # from right to max
        right_max = -1
        for i in range(len(height)-1, max_index, -1):
            if height[i] > height[right_max]:
                right_max = i
            else:
                area += (height[right_max] - height[i])
        return area
        

        