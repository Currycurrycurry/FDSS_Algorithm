class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_counter = collections.Counter(nums)
        tails = [0 for _ in range(max(nums)+1)]
        length = len(nums)
        for i in range(length):
            if num_counter[nums[i]] == 0:
                continue
            elif nums[i] - 1 >= 0 and num_counter[nums[i]] > 0 and tails[nums[i]-1] > 0:
                num_counter[nums[i]] -= 1
                tails[nums[i]-1] -= 1
                tails[nums[i]] += 1
            elif nums[i] + 1 <= max(nums) and nums[i] + 2 <= max(nums) and num_counter[nums[i]] > 0 and num_counter[nums[i]+1] > 0 and num_counter[nums[i]+2] > 0:
                num_counter[nums[i]] -= 1
                num_counter[nums[i]+1] -= 1
                num_counter[nums[i]+2] -= 1
                tails[nums[i]+2] += 1
            else:
                return False
        return True