class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        acc, res = 0, 0
        for num in nums:
            acc += num
            if acc == k: res += 1
            if acc - k in dic: res += dic[acc - k]
            dic[acc] = dic.get(acc, 0) + 1
        return res


