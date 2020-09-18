def treeToDoublyList(root): 
    def dfs(cur):
        if not cur: return
        dfs(cur.left) # 递归左子树
        if self.pre: # 修改节点引用
            self.pre.right, cur.left = cur, self.pre
        else: # 记录头节点
            self.head = cur
        self.pre = cur # 保存 cur
        dfs(cur.right) # 递归右子树
    
    if not root: return
    self.pre = None
    dfs(root)
    self.head.left, self.pre.right = self.pre, self.head
    return self.head