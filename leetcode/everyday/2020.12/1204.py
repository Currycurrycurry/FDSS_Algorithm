import collections
import heapq
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
    def isPossible(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num - 1 not in d:
                if num not in d:
                    d[num] = []
                heapq.heappush(d[num], 1)
            else:
                if num not in d:
                    d[num] = []
                ele = heapq.heappop(d[num - 1])
                if not d[num - 1]:
                    del d[num - 1]
                heapq.heappush(d[num], ele + 1)
        for v in d.values():
            if v[0] < 3:
                return False
        return True
    
    def isPossible(self, nums: List[int]) -> bool:
        # 哈希表 + 堆
        hash_map = collections.defaultdict(list)
        for num in nums:
            if hash_map.get(num-1, []):
                prev_min_len = heapq.heappop(hash_map[num - 1])
                heapq.heappush(hash_map[num], prev_min_len + 1)
            else:
                heapq.heappush(hash_map[num], 1)
        
        for num in hash_map:
            if hash_map[num] and heapq.heappop(hash_map[num]) < 3:
                return False
        
        return True