class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0 for _ in range(101)]
        for num in nums:
            bucket[num] += 1
        return [sum(bucket[0:n]) for n in nums]