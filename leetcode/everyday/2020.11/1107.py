class Solution:
    @classmethod
    def countRange(cls, nums, lower, upper):
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if lower <= sum(nums[i:j+1]) <= upper:
                    res += 1
        return res
    
