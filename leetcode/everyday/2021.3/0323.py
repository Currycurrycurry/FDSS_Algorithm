class NestedInteger:
    def __init__(self, num_or_list):
        self.num_or_list = num_or_list
    def isInteger(self):
        pass
    def getInteger(self):
        pass
    def getList(self):
        pass

class NestedIterator:
    def __init__(self, nestedList):
        self.nested_list = []
        self.point = 0
        self.add(nestedList)
    
    def add(self, nested_list):
        for ele in nested_list:
            if ele.isInteger():
                self.nested_list.append(ele.getInteger())
            else:
                self.add(ele.getList())
    
    def next(self):
        ele = self.nested_list[self.point]
        self.point += 1
        return ele
    
    def hasNext(self):
        return self.point < len(self.nested_list)

        