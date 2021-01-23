# 1.22 数组形式的整数加法
# ac用时：20min
# 和普通的整数加法好像没啥区别，但要注意进位carry和两个整数的位数的对齐

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        ans = []
        K_len = 0
        tmp_K = K
        while tmp_K:
            tmp_K //= 10
            K_len += 1
        if len(A) < K_len:
            A = [0] * (K_len - len(A)) + A
        a_index = len(A) - 1
        while a_index > -1 and (K or carry):
            val = K % 10
            target = A[a_index] + val + carry
            ans.append(target % 10)
            carry = target // 10
            K //= 10
            a_index -= 1
        if carry:
            ans.append(carry)
        while a_index > -1:
            ans.append(A[a_index])
            a_index -= 1
        return ans[::-1]

