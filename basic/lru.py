from collections import OrderedDict
# OrderedDict 算法能比 dict 更好地处理频繁的重排序操作。 如下面的例程所示，这使得它更适用于实现各种 LRU 缓存。
# 在继承 了自身的 dict 之后，类中还声明了一个循环双向链表 self.__root 作为自己的属性，
# 用另一个 dict 结构 self.__map 来存储 Key 到链表节点的对应关系，这样在更新或删除一个已有 Key 的时候，能在常数时间内完成对双向链表的操作。
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity 
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key) # 将一个现有的 key 移到序字典的任一端
            return self[key]    
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False) # 它将返回并移除最左边（开头）的条目

# LRU 算法的淘汰策略是 Least Recently Used，也就是每次淘汰那些最久没被使用的数据；
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

