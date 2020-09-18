class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i = 0
        ans = []
        while i < len(intervals):
            left, right = intervals[i][0], intervals[i][1]
            while i+1 < len(intervals) and left <= intervals[i+1][0] <= right:
                right = max(right, intervals[i+1][1])
                i += 1
            ans.append([left, right])
            i += 1
        return ans