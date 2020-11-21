class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.length = len(self.nums)
        self.tree = [0 for _ in range(1000)]
        self.build_tree(0, 0, len(self.nums) - 1)
    
    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.nums[start]
        else:
            mid = (start + end) // 2
            left_node = node * 2 + 1
            right_node = node * 2 + 2
            self.build_tree(left_node, start, mid)
            self.build_tree(right_node, mid+1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]
    
    def update(self, i, val, node=0, start=0, end=5):
        if start == end:
            self.nums[i] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if i >= start and i <= mid:
                self.update(i, val, left_node, start, mid)
            else:
                self.update(i, val, right_node, mid+1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]
    
    def query_tree(self, node=0, start=0, end=5, L=0, R=5):
        if R < start or L > end:
            return 0
        elif L <= start and end <= R:
            return self.tree[node]
        elif start == end:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            sum_left = self.query_tree(left_node, start, mid, L, R)
            sum_right = self.query_tree(right_node, mid + 1, end, L, R)
            return sum_left + sum_right
    

nums = NumArray([1, 3, 5, 7, 9, 11])

for i in range(15):
    print('tree[%d] = %d' % (i, nums.tree[i]))
for i in range(nums.length-1):
    nums.update(i, i)
    print(nums.query_tree(L=i, R=i+1))

    
    



