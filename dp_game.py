# 64. 最小路径和
def minPathSum(self, grid) -> int:
    row_len, col_len = len(grid), len(grid[0])
    for row in range(1, row_len):
        grid[row][0] += grid[row-1][0]
    for col in range(1, col_len):
        grid[0][col] += grid[0][col-1]
    for row in range(1, row_len):
        for col in range(1, col_len):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]


# 174. 地下城游戏
def calculateMinimumHP(self, dungeon) -> int:
    row_len = len(dungeon)
    col_len = len(dungeon[0])
    # base case
    dp = [[-1 for _ in range(col_len + 1)] for _ in range(row_len + 1)]
    for i in range(row_len + 1):
        dp[i][col_len] = float('inf')
    for j in range(col_len + 1):
        dp[row_len][j] = float('inf')
    # dp
    for i in range(row_len - 1, -1, -1):
        for j in range(col_len - 1, -1, -1):
            if i == row_len - 1 and j == col_len - 1:
                dp[i][j] = 1 if dungeon[i][j] >= 0 else 1 - dungeon[i][j]
            else:
                ans = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j] 
                dp[i][j] = 1 if ans <= 0 else ans
    return dp[0][0]

# 514. 自由之路


# 787. K 站中转内最便宜的航班【加权最短路径】
def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
    in_degree = [[] for _ in range(n)]
    for f in flights:
        frm, to, price = f[0], f[1], f[2]
        in_degree[to].append((frm, price))
    k = k + 1 # 将中转站个数转化成边的条数
    memo = [[-888 for _ in range(k + 1)] for _ in range(n)] # 初始化备忘录（全部填一个特殊值好判断）
    # 定义：从src出发，k步（边）之内到达dst的最短路径权重
    def dp(target, k):
        # base case
        if target == src:
            return 0
        if k == 0:
            return -1
        if memo[target][k] != -888:
            return memo[target][k]
        res = float('inf')
        for place in in_degree[target]:
            frm, price = place[0], place[1]
            sub_problem = dp(frm, k - 1)
            if sub_problem != -1:
                res = min(res, sub_problem + price)
        if res != float('inf'):
            memo[target][k] = res
        else:
            memo[target][k] = -1
        return memo[target][k]
    return dp(dst, k)

class State:
    def __init__(self, id, cost, node_num):
        self.id = id
        self.cost_from_src = cost
        self.node_num_from_src = node_num
    
    def __lt__(self, other):
        if self.cost_from_src < other.cost_from_src:
            return True
        else:
            return False

# 787. K 站中转内最便宜的航班【加权最短路径】
## 加权BFS等价于djistra缔结斯特拉算法解决
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        def generate_graph(n, flights):
            graph = [[] for _ in range(n)]
            for edge in flights:
                frm, to, weight = edge[0], edge[1], edge[2]
                graph[frm].append((to, weight))
            return graph
        graph = generate_graph(n, flights)
        print(graph)
        def dj(n, graph, src, dst, k):
            # 从起点src到达节点i的最短路径权重为dist_to[i]
            dist_to = [float('inf') for _ in range(n)] 
            # 从七点src到达节点i的最小权重路径至少要经过node_num_to[i]个节点
            node_num_to = [float('inf') for _ in range(n)]
            # base case
            dist_to[src] = 0
            node_num_to[src] = 0

            # priority queue, cost_from_src较小的排在前面
            pq = []
            heapq.heappush(pq, State(src, 0, 0))
            while len(pq) > 0:
                cur_state = heapq.heappop(pq)
                cur_node_id = cur_state.id
                cur_cost_from_src = cur_state.cost_from_src
                cur_node_num_from_src = cur_state.node_num_from_src

                if cur_node_id == dst:
                    return cur_cost_from_src

                if cur_node_num_from_src == k:
                    continue
                # 将cur_node的相邻节点装入队列
                for neighbor in graph[cur_node_id]:
                    next_node_id = neighbor[0]
                    next_node_weight = neighbor[1]
                    cost_to_next_node = cur_cost_from_src + next_node_weight
                    next_node_num_from_src = cur_node_num_from_src + 1 # 中转次数消耗1

                    # 更新dp table
                    if dist_to[next_node_id] > cost_to_next_node:
                        dist_to[next_node_id] = cost_to_next_node
                        node_num_to[next_node_id] = next_node_num_from_src

                    # 剪枝
                    if cost_to_next_node > dist_to[next_node_id] and \
                        next_node_num_from_src > node_num_to[next_node_id]:
                        continue
                    heapq.heappush(pq, State(next_node_id, cost_to_next_node, next_node_num_from_src))
            return -1
        return dj(n, graph, src, dst, k + 1)

# 10. 正则表达式匹配
## 第一次匹配：不带备忘录的递归做法
def isMatch(self, s: str, p: str) -> bool:
    memo = dict()
    s_len = len(s)
    p_len = len(p)
    def dp(i, j):
        # base case 1: s和p都匹配完全
        if j == p_len:
            return i == s_len
        # base case 2: s匹配到底，p剩余的都是*和字母的合理（可以被消掉的）组合
        if i == s_len:
            if (p_len - j) % 2 != 0:
                return False
            # 进一步判断剩余字符串是否是[字母*]的模式
            for k in range(j+1, p_len, 2):
                if p[k] != '*':
                    return False
            return True
        # core function
        # branch 1: 匹配
        if s[i] == p[j] or p[j] == '.':
            if j < p_len - 1 and p[j + 1] == '*':
                return dp(i, j + 2) or dp(i + 1, j) # 匹配0次或多次
            else:
                return dp(i + 1, j + 1) # 匹配一次
        # branch 2: 不匹配
        else:
            if j < p_len - 1 and p[j + 1] == '*':
                return dp(i, j + 2) # 匹配0次
            else:
                return False # 无法匹配
    return dp(0, 0)

## 第二次匹配：带备忘录的递归做法
def isMatch(s: str, p: str) -> bool:
    memo = dict()
    s_len = len(s)
    p_len = len(p)
    def dp(i, j):
        if (i, j) in memo.keys():
            return memo[(i, j)]
        # base case 1: s和p都匹配完全
        if j == p_len:
            return i == s_len
        # base case 2: s匹配到底，p剩余的都是*和字母的合理（可以被消掉的）组合
        if i == s_len:
            if (p_len - j) % 2 != 0:
                return False
            # 进一步判断剩余字符串是否是[字母*]的模式
            for k in range(j+1, p_len, 2):
                if p[k] != '*':
                    return False
            return True
        # core function
        res = False
        # branch 1: 匹配
        if s[i] == p[j] or p[j] == '.':
            if j < p_len - 1 and p[j + 1] == '*':
                res = dp(i, j + 2) or dp(i + 1, j) # 匹配0次或多次
            else:
                res =  dp(i + 1, j + 1) # 匹配一次
        # branch 2: 不匹配
        else:
            if j < p_len - 1 and p[j + 1] == '*':
                res = dp(i, j + 2) # 匹配0次
            else:
                res = False # 无法匹配
        memo[(i, j)] = res
        return res
    return dp(0, 0)

## 第三次匹配：DP做法，如果用DP Table较为复杂，不如直接用备忘录递归方法



# 887. 鸡蛋掉落 / 扔鸡蛋
## 【最坏情况】鸡蛋破碎一定发生在搜索区间穷尽时
# 实际上，如果不限制鸡蛋个数的话，二分思路显然可以得到最少尝试的次数，
# 但问题是，现在给你了鸡蛋个数的限制 K，直接使用二分思路就不行了。
# “如果不要「二分」，变成「五分」「十分」都会大幅减少最坏情况下的尝试次数。”
### 第一次扔鸡蛋：带备忘录的自顶向下的递归做法
#### 算法的总时间复杂度是 O(K*N^2), 空间复杂度 O(KN)
def superEggDrop(self, k: int, n: int) -> int:
    self.memo = dict()
    def dp(k, n):
        if k == 1:
            return n
        if n == 0:
            return 0
        if (k, n) in self.memo.keys():
            return self.memo[(k, n)]
        res = float('inf')
        for i in range(1, n+1):
            res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1)
        self.memo[(k, n)] = res
        return res
    return dp(k, n)

### 第二次扔鸡蛋：没有经过优化的DP做法
#### 算法的总时间复杂度是 O(K*N^2), 空间复杂度 O(KN)
def superEggDrop(k: int, n: int) -> int:
    # base case
    dp = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        dp[i][1] = n
    for i in range(1, n):
        for j in range(1, k):
            # egg not corrupt: dp[n-i][j]
            # egg corrpt: dp[i-1][j-1]
            dp[i][j] = min(max(dp[i-1][j-1], dp[n-i][j]) + 1)
    return dp[-1][-1]

### 第三次扔鸡蛋：没有经过优化的DP做法
#### 算法的总时间复杂度是 O(K*N^2), 空间复杂度 O(KN)
def superEggDrop(k: int, n: int) -> int:
    # K表示鸡蛋数量，M表示尝试次数，最多n次
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    m = 0 
    while dp[m][k] < n:
        m += 1
        for i in range(1, k+1):
            dp[m][i] = dp[m - 1][i] + dp[m - 1][i - 1] + 1
    return m

# 312. 戳气球
def maxCoins(nums) -> int:
    n = len(nums)
    points = [0 for _ in range(n + 2)]
    points[0] = points[n + 1] = 1
    for i in range(1, n+1, 1):
        points[i] = nums[i - 1]
    # base case
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    # transition
    for i in range(n, -1, -1):
        for j in range(i + 1, n+2, 1):
            for k in range(i + 1, j, 1):
                dp[i][j] = max(dp[i][j], dp[i][k] + points[i] * points[k] * points[j] + dp[k][j])
    return dp[0][n+1]

# 486. 预测赢家（用DP解决博弈问题的模板，重要）
def PredictTheWinner(nums) -> bool:
    n = len(nums)
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    # base case
    for i in range(n):
        dp[i][i][0] = nums[i]
    # transition iteration
    for i in range(n-2, -1, -1):
        for j in range(i+1, n, 1):
            left = nums[i] + dp[i+1][j][1]
            right = nums[j] + dp[i][j-1][1]
            if left > right:
                dp[i][j][0] = left
                dp[i][j][1] = dp[i+1][j][0]
            else:
                dp[i][j][0] = right
                dp[i][j][1] = dp[i][j-1][0]
    return dp[0][n-1][0] >= dp[0][n-1][1]

# 651. 4键键盘🔒
def max_a(n: int) -> int:
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j-2] * (i - j + 1))
    return dp[-1]