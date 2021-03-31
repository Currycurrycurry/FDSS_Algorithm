def dfs(nums, u, cur, ans):
    if u == len(nums):
        ans.add(tuple(cur))
        return
    cur.append(nums[u])
    dfs(nums, u+1, cur, ans)
    cur.pop()
    dfs(nums, u+1, cur, ans)

def subsetsWithDup(nums):
    nums.sort()
    ans = set()
    cur = []
    dfs(nums, 0, cur, ans)
    return [list(x) for x in ans]
    
