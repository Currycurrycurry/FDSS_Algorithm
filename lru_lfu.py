from collections import OrderedDict
# OrderedDict 算法能比 dict 更好地处理频繁的重排序操作。 如下面的例程所示，这使得它更适用于实现各种 LRU 缓存。

class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class DoubleList:
    # 头尾虚节点
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # 在链表尾部添加节点 x，时间 O(1)
    def addLast(self, x: Node):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1
    
    # 删除链表中的 x 节点（x 一定存在）
    # 由于是双链表且给的是目标 Node 节点，时间 O(1)
    def remove(self, x: Node):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
    
    # 删除链表中第一个节点，并返回该节点，时间 O(1)
    def removeFirst(self) -> Node:
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first
    
    # 返回链表长度，时间 O(1)
    def size(self) -> int:
        return self.size

class LRUCache:
    # key -> Node(key, val)
    # 创建一个哈希表将 Node 节点的 key 映射至其本身

    # Node(k1, v1) <-> Node(k2, v2)...
    # 双向链表用来实现 LRU 缓存淘汰机制

    # 最大容量
    # 缓存最大容量，超过此容量则淘汰
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.cache = DoubleList()

    def makeRecently(self, key: int):
        # 将某个 key 提升为最近使用的
        x = self.map.get(key)
        # 先从链表中删除这个节点
        self.cache.remove(x)
        # 重新插到队尾
        self.cache.append(x)

    def addRecently(self, key: int, val: int):
        # 添加最近使用的元素
        x = Node(key, val)
        # 链表尾部就是最近使用的元素
        self.cache.append(x)
        # 别忘了在 map 中添加 key 的映射
        self.map[key] = x

    def deleteKey(self, key: int):
        # 删除某一个 key
        x = self.map.get(key)
        # 从链表中删除
        self.cache.remove(x)
        # 从 map 中删除
        self.map.pop(key)

    def removeLeastRecently(self):
        # 删除最久未使用的元素
        # 链表头部的第一个元素就是最久未使用的
        deletedNode = self.cache.pop(0)
        # 同时别忘了从 map 中删除它的 key
        deletedKey = deletedNode.key
        self.map.pop(deletedKey)

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        # 将该数据提升为最近使用的
        self.makeRecently(key)
        return self.map[key].val

    def put(self, key: int, val: int) -> None:
        if key in self.map:
            # 删除旧的数据
            self.deleteKey(key)
            # 新插入的数据为最近使用的数据
            self.addRecently(key, val)
            return

        if self.cap == len(self.cache):
            # 删除最久未使用的元素
            self.removeLeastRecently()
        # 添加为最近使用的元素
        self.addRecently(key, val)

    
# 【使用OrderedDict API实现】LRU 算法的淘汰策略是 Least Recently Used，也就是每次淘汰那些最久没被使用的数据；
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity # # 缓存最大容量

    def get(self, key: int) -> int:
        if key not in self:
            return -1 # 返回-1表示查找失败
        else:
            self.move_to_end(key) # # 将当前访问的节点移到双向链表尾部
            return self[key]    
        
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key) # 将当前访问的节点移到双向链表尾部
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) # 双向链表头部为最久没有被访问的节点，删除该节点


# 而 LFU 算法的淘汰策略是 Least Frequently Used，也就是每次淘汰那些使用次数最少的数据。
class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 0
        super(LFUNode, self).__init__(key, value)
 
class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        # key: 频率, value: 频率对应的双向链表
        self.freq_map = {}
        self.size = 0
 
    # 更新节点频率的操作
    def __update_freq(self, node):
        freq = node.freq
 
        # 删除
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
 
        # 更新
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)
 
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value
 
    def put(self, key, value):
        if self.capacity == 0:
            return
 
        # 缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)
 
        # 缓存没有命中
        else:
            if self.capacity == (min_freq:=min(self.freq_map)):
                node = self.freq_map[min_freq].pop()
                del self.map[node.key]
                self.size -= 1
            node = LFUNode(key, value)
            node.freq = 1
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            node = self.freq_map[node.freq].append(node)
            self.size += 1

c = LRUCache(5)
  
for i in range(5,10):
    c.set(i,10*i)
  
  
print (c.cache, c.cache.keys())
  
c.get(5)
c.get(7)
  
print (c.cache, c.cache.keys())
  
c.set(10,100)
print (c.cache, c.cache.keys())
  
c.set(9,44)
print (c.cache, c.cache.keys())

