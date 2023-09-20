# O(n2) O(n2) o(n) o(1) stable easy
def insertionSort(arr):
    for i in range(len(arr) - 1):
        current = arr[i]
        preIndex = i - 1
        while preIndex >= 0 and current < arr[preIndex]:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr

# O(n1.3) / / O(1) unstable complex
def shellSort(arr):
    pass

# O(n2) O(n2) O(n2) O(1) stable easy
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        cnt = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr [j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
        if cnt == 0:
            break
    return arr

# O(nlogn) O(nlogn) O(nlogn) O(nlogn) stable complex
def partition(arr, left, right):
    pivot = left
    left_index = left + 1
    right_index = right
    while left_index < right_index:
        while left_index < len(arr) - 1 and arr[left_index] < arr[pivot]:
            left_index += 1
        while right_index > 0 and arr[right_index] > arr[pivot]:
            right_index -= 1
        if left_index < right_index:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    arr[pivot], arr[right_index] = arr[right_index], arr[pivot]
    return right_index

def quickSort(arr, left, right):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        index = partition(arr, left, right)
        quickSort(arr, left, index - 1)
        quickSort(arr, index + 1, right)
    return arr

arr = [5, 1, 3, 9, 2]
print(quickSort(arr, 0, len(arr) - 1))

# O(n2) O(n2) O(n2) O(1) stable easy
def selectSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# O(nlogn) O(nlogn) o(nlogn) O(n) stable complex
def mergeSort(arr):        
    if arr:
        mid = len(arr) // 2
        left = mergeSort(arr[0:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    else:
        return []

def merge(left, right):
    res = []
    while left and right:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res

# O(nlogn) O(nlogn) O(nlogn) O(1) stable complex
def heapSort(arr):
    heap_size = len(arr)
    buildHeap(arr)
    for i in range(len(arr)):
        arr[0], arr[heap_size - 1] = arr[heap_size - 1], arr[0]
        heap_size -= 1
        heapify(arr, 0, heap_size)

def buildHeap(arr):
    for i in range(len(arr)//2, 0, -1):
        heapify(arr, i, len(arr))

def heapify(arr, i, heap_size):
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    largest = i
    if left_child_index < heap_size and arr[left_child_index] > arr[i]:
        largest = left_child_index
    if right_child_index < heap_size and arr[right_child_index] > arr[i]:
        largest = right_child_index
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, heap_size)

def radixSort(arr):
    current_index = 0
    max_num = max(arr)
    max_num_len = len(str(max_num))

    while current_index < max_num_len:
        bucket_list = [[] for _ in range(10)]
        for num in arr:
            bucket_list[int(num/10**current_index) % 10].append(num)
        arr.clear()
        for nums in bucket_list:
            for num in nums:
                arr.append(num)
        current_index += 1

# 链表归并排序 merge sort
def sortList(head):
    def sortFunc(head, tail):
        # base case: None
        if not head:
            return head
        # base case: only one node
        if head.next == tail:
            head.next = None
            return head
        # 找到中间节点
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow # 此时slow就指向中间
        return merge(sortFunc(head, mid), sortFunc(mid, tail))
        
    def merge(head1, head2):
        dummyHead = Node(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummyHead.next
    
# 链表冒泡排序
def bubbleSort(head: Node):
    node_i = head
    tail = None
    # 外层循环次数为 链表节点个数
    while node_i:
        node_j = head
        while node_j and node_j.next != tail:
            if node_j.val > node_j.next.val:
                # 交换两个节点的值
                node_j.val, node_j.next.val = node_j.next.val, node_j.val
            node_j = node_j.next
        # 尾指针向前移动 1 位，此时尾指针右侧为排好序的链表
        tail = node_j
        node_i = node_i.next
    return head

# 链表选择排序
def sectionSort(head: Node):
    node_i = head
    # node_i 为当前未排序链表的第一个链节点
    while node_i and node_i.next:
        # min_node 为未排序链表中的值最小节点
        min_node = node_i
        node_j = node_i.next
        while node_j:
            if node_j.val < min_node.val:
                min_node = node_j
            node_j = node_j.next
        # 交换值最小节点与未排序链表中第一个节点的值
        if node_i != min_node:
            node_i.val, min_node.val = min_node.val, node_i.val
        node_i = node_i.next
    
    return head

def partition(self, left: ListNode, right: ListNode):
    # 左闭右开，区间没有元素或者只有一个元素，直接返回第一个节点
    if left == right or left.next == right:
        return left
    # 选择头节点为基准节点
    pivot = left.val
    # 使用 node_i, node_j 双指针，保证 node_i 之前的节点值都小于基准节点值，node_i 与 node_j 之间的节点值都大于等于基准节点值
    node_i, node_j = left, left.next
    
    while node_j != right:
        # 发现一个小与基准值的元素
        if node_j.val < pivot:
            # 因为 node_i 之前节点都小于基准值，所以先将 node_i 向右移动一位（此时 node_i 节点值大于等于基准节点值）
            node_i = node_i.next
            # 将小于基准值的元素 node_j 与当前 node_i 换位，换位后可以保证 node_i 之前的节点都小于基准节点值
            node_i.val, node_j.val = node_j.val, node_i.val
        node_j = node_j.next
    # 将基准节点放到正确位置上
    node_i.val, left.val = left.val, node_i.val
    return node_i
    
def quickSort(self, left: ListNode, right: ListNode):
    if left == right or left.next == right:
        return left
    pi = self.partition(left, right)
    self.quickSort(left, pi)
    self.quickSort(pi.next, right)
    return left

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    return self.quickSort(head, None)