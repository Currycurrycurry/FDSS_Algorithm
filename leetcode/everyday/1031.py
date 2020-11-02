class RandomizedCollection:
    def __init__(self):
        self.index_dict = dict()
        self.arr_space = []
    
    def addElement(self, val):
        self.arr_space.append()
        if val in self.index_dict:
            self.index_dict.add(len(self.arr_space) - 1)
            return True
        else:
            self.index_dict = {len(self.arr_space) - 1}
            return False
    
    def delElement(self, val):
        if val not in self.index_dict:
            return False
        last_index = len(self.arr_space) - 1
        cur_index = self.index_dict[val].pop()
        if cur_index != last_index:
            self.arr_space[cur_index] = self.arr_space[last_index]
            self.index_dict[self.arr_space[cur_index]].remove(last_index)
            self.index_dict[self.arr_space[cur_index]].add(cur_index)
        self.arr_space.pop()
        return True

    def getRandomElement(self):
        import random
        return self.arr_space[int(random.random()*len(self.arr_space))]

        