class Solution:
    # buggy
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                # find next min num
                next_min_index = i
                tmp_index = i
                while tmp_index < len(nums):
                    if nums[next_min_index] > nums[tmp_index]:
                        next_min_index = tmp_index
                    tmp_index += 1
                nums[next_min_index], nums[i-1] = nums[i-1], nums[next_min_index]
                # sort
                print(i)
                for j in range(i, len(nums)):
                    for k in range(i, len(nums) - j):
                        if nums[k] > nums[k + 1]:
                            nums[k], nums[k+1] = nums[k+1], nums[k]
                break
            i -= 1
    
    # bugfree
    def nextPermutation2(self, nums):
        left_pointer = len(nums) - 2
        while left_pointer >= 0 and nums[left_pointer] > nums[left_pointer+1]:
            left_pointer -= 1
        right_pointer = len(nums) - 1
        while right_pointer >= 0 and nums[right_pointer] < nums[left_pointer]:
            right_pointer -= 1
        nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
        l, r = left_pointer + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[l], nums[r]
            l += 1
            r -= 1


