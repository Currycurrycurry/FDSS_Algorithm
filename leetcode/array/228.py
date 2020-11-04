class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        p,ans = 0,[]
        while p < len(nums):
            start = end = nums[p]
            while p+1 < len(nums) and nums[p]+1 == nums[p+1]:
                p += 1
                end = nums[p]
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")
            p += 1
        return ans