ans = []
def sum_of_k_nums(sum, n, val):
    if val > sum or n <= 0:
        return
    if val == sum:
        print(ans)
        # return True
    ans.append(n)
    sum_of_k_nums(sum, n - 1, val + n)
    ans.remove(n)
    sum_of_k_nums(sum, n - 1, val)
sum_of_k_nums(5, 10, 0)


def minPatches(self, nums: List[int], n: int) -> int:
    res = 0
    left = right = 0
    i = 0
    target = 1
    while right < n:
        if i >= len(nums) or (i < len(nums) and nums[i] > target):
            res += 1
            right += target
        elif i < len(nums):
            right += nums[i]
            i += 1
        target = right + 1
    return res

    
def minPatches(self, nums: List[int], n: int) -> int:
    res = 0
    index = 0
    x = 1
    while x <= n:
        if index < len(nums) and nums[index] <= x:
            x += nums[index]
            index += 1
        else:
            res += 1
            x <<= 1
    return res



