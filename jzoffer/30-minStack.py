class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def min(self):
        return self.minStack[-1]
    
    def push(self, val):
        self.stack.append(val)
        if self.minStack:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    
    def pop(self, val):
        self.stack.pop()
        self.minStack.pop()


minStack1 = minStack()
minStack1.push(1)
minStack1.push(-1)
minStack1.push(-2)
print(minStack1.min())

