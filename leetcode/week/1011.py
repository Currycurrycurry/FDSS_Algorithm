class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        import numpy as np
        roads = np.array(roads)
        roads = roads.flatten()
        road_nums = [roads.count(i) for i in range(n)]
        # 找出数组最大的三个数
        max_value = max(road_nums)
        