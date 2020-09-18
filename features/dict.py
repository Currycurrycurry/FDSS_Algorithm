class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = dict()
        max_length = 0
        for num in nums:
            if num not in hash_dict.keys():
                left_num = hash_dict.get(num-1, 0)
                right_num = hash_dict.get(num+1, 0)
                cur_value = left_num + right_num + 1
                hash_dict[num - left_num] = cur_value
                hash_dict[num + right_num] = cur_value
                hash_dict[num] = cur_value
                if hash_dict[num] > max_length:
                    max_length = hash_dict[num]
        return max_length


        