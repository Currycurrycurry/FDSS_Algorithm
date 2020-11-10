import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        c = collections.Counter(s)
        seen = set()
        res = 0
        for k, v in c.items():
            cur = v
            while cur>0 and cur in seen:
                cur -= 1
            res += v - cur
            if cur>0:
                seen.add(cur)
        return res
    
    def minDeletions(self, s: str) -> int:
        s_set = set(s)
        s_dict = dict()
        for i in s_set:
            s_dict[i] = s.count(i)
        val_arr = list(s_dict.values())
        # print(val_arr)
        val_arr.sort()
        # print(val_arr)
        delete_target = 0
        cnt = 0
        for i in range(len(val_arr)-1):
            if val_arr[i] == val_arr[i+1]:
                delete_target = 0
                for j in range(val_arr[i], -1, -1):
                    if j not in val_arr:
                        delete_target = j
                        break
                cnt += (val_arr[i] - delete_target)
                val_arr[i] = delete_target
        # print(val_arr)
        return cnt
