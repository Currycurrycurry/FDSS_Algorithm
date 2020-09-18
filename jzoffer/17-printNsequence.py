class Solution:
    def __init__(self):
        self.res = []
    def printNumbers(self, n: int) -> List[int]:
        if n == 0:
            return []
        nums = ['' for i in range(n)]
        def printNum(nums, index):
            if index == n:
                self.res.append(int(''.join(nums)))
                return None
            for i in range(0, 10):
                nums[index] = str(i)
                printNum(nums, index + 1)
        for i in range(0, 10):
            nums[0] = str(i)
            printNum(nums, 1)

        return self.res[1:]  


