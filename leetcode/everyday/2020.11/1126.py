class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def radix_sort(nums):
            max_num = max(nums)
            max_num_len = len(str(max_num))
            i = 0
            while i < max_num_len:
                bucket_list = [[] for _ in range(10)]
                for num in nums:
                    bucket_list[int(num/10**i) % 10].append(num)
                nums.clear()
                for num_list in bucket_list:
                    for num in num_list:
                        nums.append(num)
                i += 1
        if not nums: 
            return 0
        radix_sort(nums)
        max_gap = 0
        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i+1] - nums[i])
        return max_gap
    

    def maximumGap(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = max(nums)
        min_val = min(nums)
        if max_val == min_val:
            return 0
        d = (max_val - min_val) // len(nums) or 1
        bucket_size = (max_val - min_val) // d + 1
        buckets = [[-1 for _ in range(2)] for _ in range(bucket_size)]

        for num in nums:
            index = (num - min_val) // d
            if buckets[index][0] == -1:
                buckets[index][0] = buckets[index][1] = num
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)
        max_gap = 0
        prev = -1
        for i in range(bucket_size):
            if buckets[i][0] == -1:
                continue
            if prev != -1:
                max_gap = max(max_gap, buckets[i][0] - buckets[prev][1])
            prev = i
        return max_gap