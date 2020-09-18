def getLeastNumbers(arr, k): 
    def heapify(arr, i, heap_size):
        smallest = i
        left_p = 2 * i + 1
        right_p = 2 * i + 2
        if left_p < heap_size and arr[smallest] > arr[left_p]:
            smallest = left_p
        if right_p < heap_size and arr[smallest] > arr[right_p]:
            smallest = right_p
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            heapify(arr, smallest, heap_size)
    def buildHeap(arr):
        for i in range(len(arr)//2, -1, -1):
            heapify(arr, i, len(arr))  
    if not arr: return  
    buildHeap(arr)
    cnt = len(arr) - 1
    ans = []
    for cnt in range(len(arr) - 1, len(arr) - 1 - k, -1):
        ans.append(arr[0])
        arr[0], arr[cnt] = arr[cnt], arr[0]
        heapify(arr, 0, cnt)
    return ans


def getLeastNumbers2(arr, k): 
    if k == 0:
        return []
    heap_arr = [-k for k in arr[:k]]
    heapq.heapify(heap_arr)
    for i in arr[k:]:
        if i < -heap_arr[0]:
            heapq.heappop(heap_arr)
            heapq.heappush(heap_arr, -i)
    return [-k for k in heap_arr]

def partition(nums, l, r):
    pivot = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1

def randomized_partition(nums, l, r):
    i = random.randint(l, r)
    nums[r], nums[i] = nums[i], nums[r]
    return self.partition(nums, l, r)

def randomized_selected(arr, l, r, k):
    pos = self.randomized_partition(arr, l, r)
    num = pos - l + 1
    if k < num:
        self.randomized_selected(arr, l, pos - 1, k)
    elif k > num:
        self.randomized_selected(arr, pos + 1, r, k - num)

def getLeastNumbers(arr: List[int], k: int) -> List[int]:
    if k == 0:
        return list()
    self.randomized_selected(arr, 0, len(arr) - 1, k)
    return arr[:k]
