class Solution:
    def count_range_sum(self, nums, lower, upper):
        def count_range_sum_recursive(pre_sum, lower, upper, left, right):
            if left == right:
                return 0
            mid = (left + right) // 2
            n1 = count_range_sum_recursive(pre_sum, lower, upper, left, mid)
            n2 = count_range_sum_recursive(pre_sum, lower, upper, mid + 1, right)
            ret = n1 + n2

            i = left
            l = mid + 1
            r = mid + 1
            while i <= mid:
                while l <= right and pre_sum[l] - pre_sum[i] < lower:
                    l += 1
                while r <= right and pre_sum[r] - pre_sum[i] <= upper:
                    r += 1
                ret += (r - l)
                i += 1
        s = 0
        pre_sum = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            s +=nums[i]
            pre_sum[i+1] = s
        return count_range_sum_recursive(pre_sum, lower, upper, 0, len(pre_sum) - 1)
    
    

        
