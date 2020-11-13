class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # buggy: simulate the whole process greekly
        ring_index = 0
        length = len(ring)
        res = 0
        for letter in key:
            forward_step, backward_step = 0, 0
            # forward search
            forward_i = ring_index
            while forward_i < length:
                if ring[forward_i] == letter:
                    break
                forward_i += 1
                forward_step += 1
    
            # backward search
            backward_i = ring_index
            while backward_i >= 0:
                if ring[backward_i] == letter:
                    break
                backward_i -= 1
                backward_step += 1
            if forward_step > backward_step:
                res += backward_step
                ring_index = backward_i
            else:
                res += forward_step
                ring_index = forward_i
        return res
    
        # buggy dfs method: 每一步最近不代表整体路径最短
    def findRotateSteps(self, ring: str, key: str) -> int:
        length = len(ring)
        def dfs(ring_index, key_index):
            if key_index == len(key):
                return 0 
            forward_step, backward_step = 0, 0
            # forward search
            forward_i = ring_index
            while forward_i < length:
                if ring[forward_i] == key[key_index]:
                    break
                forward_i += 1
                forward_step += 1
    
            # backward search
            backward_i = ring_index
            while backward_i >= 0:
                if ring[backward_i] == key[key_index]:
                    break
                backward_i -= 1
                backward_step += 1

            if forward_step > backward_step:
                return dfs(backward_i, key_index+1) + backward_step
            else:
                return dfs(forward_i, key_index+1) + forward_step
        return dfs(0)
    

    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        pos = [[] for _ in range(26)]
        dp = [[float('inf') for _ in range(ring_len)] for _ in range(key_len)]
        for i in range(ring_len):
            pos[ord(ring[i]) - ord('a')].append(i)
        key_0_poses = pos[ord(key[0]) - ord('a')]
        for i in range(ring_len):
            if i in key_0_poses:
                dp[0][i] = min(dp[0][i], min(i, ring_len - i) + 1)
        for key_index in range(1, key_len):
            key_index_poses = pos[ord(key[key_index]) - ord('a')]
            pre_key_index_poses = pos[ord(key[key_index-1]) - ord('a')]
            for pre_k in pre_key_index_poses:
                for k in key_index_poses:
                    dp[key_index][k] = min(dp[key_index][k], dp[key_index-1][pre_k] + min(abs(pre_k - k), ring_len - abs(k - pre_k)) + 1)
        return min(dp[-1])

    # buggy
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        def helper(height_index, col_index):
            if height_index == height:
                return 0
            length = len(triangle[height_index])
            if col_index < 0 or col_index >= length:
                return 0
            if col_index == 0 or triangle[height_index][col_index+1] < triangle[height_index][col_index]:
                return triangle[height_index][col_index+1] + helper(height_index+1, col_index+1)
            elif col_index == length - 1 or triangle[height_index][col_index+1] > triangle[height_index][col_index]:
                return triangle[height_index][col_index] + helper(height_index+1, col_index)
        return helper(0, 0)
