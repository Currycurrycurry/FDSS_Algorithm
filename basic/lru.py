from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
     
    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]
         
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

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

