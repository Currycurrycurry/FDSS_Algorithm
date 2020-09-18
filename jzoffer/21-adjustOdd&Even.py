class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        left_p, right_p = 0, len(nums) - 1
        while True:
            while left_p < len(nums) and nums[left_p] % 2 == 1:
                left_p += 1
            while right_p > 0 and nums[right_p] % 2 == 0:
                right_p -= 1
            if left_p >= right_p:
                break
            nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
        return nums
