class cmp(str):
    def __lt__(self, other):
        return self + other < other + self

def minNumber(nums):
    nums = sorted([str(i) for i in nums], key=cmp)
    return ''.join(nums)

def minNumber2(self, nums: List[int]) -> str:
    from functools import cmp_to_key
    def compare(a, b):
        return 1 if a+b > b+a else -1
    nums = sorted([str(i) for i in nums], key=cmp_to_key(compare))
    return ''.join(nums)


def minNumber3(self, nums: List[int]) -> str:
    def fast_sort(l , r):
        if l >= r: return
        i, j = l, r
        while i < j:
            while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -= 1
            while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[l] = strs[l], strs[i]
        fast_sort(l, i - 1)
        fast_sort(i + 1, r)

    strs = [str(num) for num in nums]
    fast_sort(0, len(strs) - 1)
    return ''.join(strs)

def minNumber(nums):
    def sort_rule(x, y):
        a, b = x + y, y + x
        if a > b: return 1
        elif a < b: return -1
        else: return 0
    strs = [str(num) for num in nums]
    strs.sort(key = functools.cmp_to_key(sort_rule))
    return ''.join(strs)
