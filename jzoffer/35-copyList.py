def copyRandomList1(self, head: 'Node') -> 'Node':
    visited = {}
    def helper(head):
        if not head: return None
        if head in visited: return visited[head] 
        node = Node(head.val, None, None)
        visited[head] = node
        node.next = helper(head.next)
        node.random = helper(head.random)
        return node
    return helper(head)

def copyRandomList2(self, head: 'Node') -> 'Node':
    visited = {}
    if not head:
        return head
    clone  = Node(head.val, None, None)
    queue = collections.deque()
    queue.append(head)
    visited[head] = clone
    while queue:
        tmp = queue.popleft()
        if tmp.next and tmp.next not in visited:
            visited[tmp.next] = Node(tmp.next.val, [], [])
            queue.append(tmp.next)
        if tmp.random and tmp.random not in visited:
            visited[tmp.random] = Node(tmp.random.val, [], [])
            queue.append(tmp.random)
        visited[tmp].next = visited.get(tmp.next)
        visited[tmp].random = visited.get(tmp.random)
    return clone

def copyRandomList3(self, head: 'Node') -> 'Node':
    visited = {}
    def helper(head):
        def getClonedNode(head):
            if not head: return None
            if head not in visited:
                visited[head] = Node(head.val, None, None)
            return visited[head]
        if not head:
            return None
        old_node = head
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node

        while old_node:    
            new_node.next = getClonedNode(old_node.next)
            new_node.random = getClonedNode(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return visited[head]
    return helper(head)

def copyRandomList4(self, head: 'Node') -> 'Node':
    if not head: return head
    cur = head
    while cur:
        new_node = Node(cur.val,None,None)   # 克隆新结点
        new_node.next = cur.next
        cur.next = new_node   # 克隆新结点在cur 后面
        cur = new_node.next   # 移动到下一个要克隆的点
    cur = head

    while cur:  # 链接random
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    cur_old_list = head # 将两个链表分开
    cur_new_list = head.next
    new_head = head.next
    while cur_old_list:
        cur_old_list.next = cur_old_list.next.next
        cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
        cur_old_list = cur_old_list.next
        cur_new_list = cur_new_list.next
    return new_head





