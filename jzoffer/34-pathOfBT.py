def pathSum(root, sum_):
    ret = []
    if not root:
        return ret
    path = [root]
    sums = [root.val]

    def dfs(root):
        if root.left:
            path.append(root.left)
            sums.append(sums[-1] + root.left.val)
            dfs(root.left)
        if root.right:
            path.append(root.right)
            sums.append(sums[-1] + root.right.val)
            dfs(root.right)
        if not root.left and not root.right:
            if sums[-1] == sum_:
                ret.append([p.val for p in path])
        path.pop()
        sums.pop()
    
    dfs(root)
    return ret