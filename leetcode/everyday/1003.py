class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()
        for i, num in enumerate(nums):
            if (target - num) in num_index.keys() :
                return (num_index[target- num], i)
            else:
                num_index[num] = i
        return -1