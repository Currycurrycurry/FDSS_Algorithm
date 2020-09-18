# wa -> ac
class Solution:
    def search(self, nums, target):
        def getFirstK(nums, target, start, end):
            mid = (start + end) // 2
            if start <= end:
                if nums[mid] == target:
                    if (mid >= 1 and nums[mid - 1] != target) or mid == 0:
                        return mid
                    else:
                        end = mid - 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                return getFirstK(nums, target, start, end)
            return -1 

        def getLastK(nums, target, start, end):
            mid = (start + end) // 2
            if start <= end:
                if nums[mid] == target:
                    if (mid <= len(nums) - 2 and  nums[mid + 1] != target) or mid == len(nums) - 1:
                        return mid
                    else:
                        start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
                return getLastK(nums, target, start, end)
            return -1

        first_k = getFirstK(nums, target, 0, len(nums) - 1)
        last_k = getLastK(nums, target, 0, len(nums) - 1)
        if first_k != -1 and last_k != -1:
           return (last_k - first_k + 1)
        else:
            return 0

class Solution:
    def missingNumber(self, nums):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i

# 数组中数值和下标相等的元素
# nums = [-3, -1, 1, 3, 5]

def findIndexValueEqualEle(nums):
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            right_pointer = mid - 1
        else:
            left_pointer = mid + 1

print(findIndexValueEqualEle([-3, -1, 1, 3, 5]))