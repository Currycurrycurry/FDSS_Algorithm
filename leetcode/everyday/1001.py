class Solution:
    # 我是什么新型睿智吗？？？
    def minimumOperations(self, leaves: str) -> int:
        if len(leaves) <= 2:
            return -1
        cnt = 0
        leaves = list(leaves)
        if leaves[0] == 'y':
            leaves[0] = 'r'
            cnt += 1
        if leaves[-1] == 'y':
            leaves[-1] = 'r'
            cnt += 1
        left_pointer, right_pointer = 1, len(leaves) - 2
        if left_pointer == right_pointer and leaves[left_pointer] == 'r':
            return cnt + 1
        if 'y' not in leaves:
            return 1
        if 'r' not in leaves[left_pointer: right_pointer+1]:
            return cnt
        else:
            while left_pointer < len(leaves) - 1 and leaves[left_pointer] == 'r':
                left_pointer += 1   
            while right_pointer > 0 and leaves[right_pointer] == 'r':
                right_pointer -= 1
            # r...ry....y y...yr...r y...y
            # 分三种情况讨论
            left_y_r_patition = left_pointer
            right_y_r_patition = right_pointer
            while left_y_r_patition < right_y_r_patition and leaves[left_y_r_patition] == 'y':
                left_y_r_patition += 1
            while right_y_r_patition > left_y_r_patition and leaves[right_y_r_patition] == 'y':
                right_y_r_patition -= 1

            val1 = leaves[left_y_r_patition:right_pointer+1].count('y')
            val2 = leaves[left_pointer:right_y_r_patition+1].count('y')
            val3 = leaves[left_y_r_patition:right_y_r_patition+1].count('r')
            cnt += min(val1, val2, val3)
        return cnt
    
    # wrong
    def minimumOperations2(self, leaves: str) -> int:
        dp = [[float('inf')] * len(leaves)] * 3
        dp[0][0] = int(leaves[0] == 'y')
        print(dp[0][0])
        # dp[1][0] = dp[2][0] = dp[2][1] = float('inf')
        for i in range(1, len(leaves)):
            is_yellow = int(leaves[i] == 'y')
            is_red = int(leaves[i] == 'r')
            dp[0][i] = dp[0][i-1] + is_yellow
            dp[1][i] = min(dp[1][i-1], dp[0][i-1]) + is_red
            if i >= 2:
                dp[2][i] = min(dp[2][i-1], dp[1][i-1]) + is_yellow
        print(dp)
        return dp[2][-1]

    # correct
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        f = [[0, 0, 0] for _ in range(n)]
        f[0][0] = int(leaves[0] == "y")
        f[0][1] = f[0][2] = f[1][2] = float("inf")

        for i in range(1, n):
            isRed = int(leaves[i] == "r")
            isYellow = int(leaves[i] == "y")
            f[i][0] = f[i - 1][0] + isYellow
            f[i][1] = min(f[i - 1][0], f[i - 1][1]) + isRed
            if i >= 2:
                f[i][2] = min(f[i - 1][1], f[i - 1][2]) + isYellow
        return f[n - 1][2]

print(Solution().minimumOperations2('rrrr'))