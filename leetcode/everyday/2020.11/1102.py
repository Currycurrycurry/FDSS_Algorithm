class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        bigger_nums, smaller_nums = nums1, nums2
        if len(nums1) < len(nums2):
            bigger_nums, smaller_nums = nums2, nums1
        for num in smaller_nums:
            if num in bigger_nums:
                res.add(num)
        return list(res)

    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    