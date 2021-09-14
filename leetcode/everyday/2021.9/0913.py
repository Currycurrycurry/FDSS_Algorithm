# 447
import math
import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        hash_map = dict()
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dis = math.pow((points[i][0] - points[j][0]), 2) + \
                        math.pow((points[i][1] - points[j][1]), 2)
                    if dis not in hash_map.keys():
                        hash_map[dis] = 1
                    else:
                        n = hash_map[dis]
                        ans += 2 * n
                        hash_map[dis] += 1
            hash_map.clear()
        return ans

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            cnt = defaultdict(int)
            for q in points:
                dis = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])
                cnt[dis] += 1
            for m in cnt.values():
                ans += m * (m - 1)
        return ans

