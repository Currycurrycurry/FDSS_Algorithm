from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 不会做
        t_dict = defaultdict(int)
        for ch in t:
            t_dict[ch] += 1
        t_len = len(t)
        left = 0
        minL, minR = 0, len(s)
        for right, ch in enumerate(s):
            if t_dict[ch] > 0:
                t_len -= 1
            t_dict[ch] -= 1

            if t_len == 0:
                while t_dict[s[left]] < 0:
                    t_dict[s[left]] += 1
                    left += 1
                if right - left < minR - minL:
                    minL, minR = left, right
                
                t_dict[s[left]] += 1
                left += 1
                t_len += 1
        return '' if minR == len(s) else s[minL:minR+1]


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        n = 0
        for i in range(len(s)):
            if s[i] == 'R':
                n += 1
            if s[i] == 'L':
                n -= 1
            if n == 0:
                num += 1
        return num

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 先对所有区间按左端点升序排序，如果左端点相同，按右端点升序排序，这样一来如果有覆盖，一定是前面的覆盖后面的
        temp = sorted(intervals, key=lambda i:(i[0], -i[1]), reverse=True)
        ans = s = len(temp)
        for i in range(s - 1):
            for j in range(i+1, s):
                if temp[i][1] <= temp[j][1]:
                    ans -= 1
                    break
        return ans