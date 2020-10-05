class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]: continue
            if nums[a] * 4 > target: break
            if nums[a] + nums[-1] * 3 < target: continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]: continue
                if nums[a] + nums[b] * 3 > target: break
                if nums[a] + nums[b] + nums[-1] * 2 < target: continue
                c, d = b + 1, n - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c + 1] == nums[c]:
                            c += 1
                        while c < d and nums[d - 1] == nums[d]:
                            d -= 1
                        c += 1
                        d -= 1
        return res