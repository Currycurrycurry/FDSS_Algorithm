def maxValueOfQueue(arr, k):
    if not arr or not k:
        return None
    if k >= len(arr):
        return [max(arr)]
    from collections import deque
    max_queue = deque()
    ans =[]
    for index, value in enumerate(arr):
        if len(max_queue) == 0:
            max_queue.append(index)
        else:
            if index - max_queue[0] >= k:
                max_queue.popleft()
            if value > arr[max_queue[0]]:
                max_queue.clear()
                max_queue.append(index)
            elif value < arr[max_queue[-1]]:
                max_queue.append(index)
            elif arr[max_queue[-1]] < value < arr[max_queue[0]]:
                max_queue.pop()
                max_queue.append(index)
        if index >= k - 1:
            ans.append(arr[max_queue[0]])
    return ans

class MaxQueue:
    def __init__(self):
        self.max_queue = collections.deque()
        self.window = collections.deque()

    def max_value(self) -> int:
        if len(self.max_queue) == 0:
            return -1
        return self.max_queue[0]

    def push_back(self, value: int) -> None:
        while self.max_queue and value > self.max_queue[-1]:
            self.max_queue.pop()
        self.window.append(value)
        self.max_queue.append(value)

    def pop_front(self) -> int:
        if len(self.window) == 0:
            return -1
        val = self.window[0]
        if val == self.max_queue[0]:
            self.max_queue.popleft()
        return self.window.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                