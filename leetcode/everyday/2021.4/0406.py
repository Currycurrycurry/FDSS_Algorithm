# stupid double pointer
# correct
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        res_p = 2
        nums_p = 2
        while True:
            while nums_p < len(nums) and nums[nums_p] == nums[res_p - 1] == nums[res_p - 2]:
                nums_p += 1
            if nums_p == len(nums):
                return res_p
            # print(res_p)
            # print(nums_p)
            nums[res_p] = nums[nums_p]
            nums_p += 1
            res_p += 1
            # print(res_p)
    
