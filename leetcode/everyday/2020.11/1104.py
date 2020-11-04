class Solution:
    def merge(self, intervals, new_interval):
        left, right = new_interval[0], new_interval[1]
        i = 0
        res = []
        while i < len(intervals):
            if left > intervals[i][1] or right < intervals[i][0]:
                res.append(intervals[i])
            else:
                left, right = min(left, intervals[i][0]), max(right, intervals[i][1])
            i += 1
        res.append([left, right])
        return sorted(res, key=lambda x:x[0])
    
    def merge(self, intervals, new_interval):
        left, right = newInterval[0], newInterval[1]
        i = 0
        res = []
        placed = False
        while i < len(intervals):
            if left > intervals[i][1]:
                res.append(intervals[i])
            elif right < intervals[i][0]:
                if not placed:
                    res.append([left, right])
                    placed = True
                res.append(intervals[i])
            else:
                left = min(left, intervals[i][0])
                right = max(right, intervals[i][1])
            i += 1
        if not placed:
            res.append([left, right])
        return res

