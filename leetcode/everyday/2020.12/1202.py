# 40 移掉K位数字
# https://leetcode-cn.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'

# 316. 去除重复字母
# https://leetcode-cn.com/problems/remove-duplicate-letters/
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        stack = []
        counter = collections.Counter(s)
        for letter in s:
            if letter not in seen:
                while stack and stack[-1] > letter and counter[stack[-1]] != 0:
                    val = stack.pop()
                    seen.discard(val)
                seen.add(letter)
                stack.append(letter)
            counter[letter] -= 1
        return ''.join(stack)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)
        for letter in s:
            if letter not in stack:
                while stack and stack[-1] > letter and counter[stack[-1]] != 0:
                    stack.pop()
                stack.append(letter)
            counter[letter] -= 1
        return ''.join(stack)


class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick_max(nums, k):
            stack = []
            drop = len(nums) - k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(A, B):
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        return max(merge(pick_max(nums1, i), pick_max(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))