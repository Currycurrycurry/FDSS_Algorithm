class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        original_val = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                original_val += customers[i]
        extra_val = 0
        left = 0
        right = 0
        tmp = 0
        while right < len(customers):
            if right < X:
                if grumpy[right] == 1:
                    tmp += customers[right] 
            else:
                tmp_right = customers[right] if grumpy[right] == 1 else 0
                tmp_left = customers[left] if grumpy[left] == 1 else 0
                tmp += tmp_right - tmp_left
                left += 1
            right += 1
            # print(tmp)
            extra_val = max(extra_val, tmp)
        # print(extra_val)
        # print(original_val)
        return extra_val + original_val

