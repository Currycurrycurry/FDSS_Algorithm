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
def quickSort(arr, left, right):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        index = partition(arr, left, right)
        quickSort(arr, left, index - 1)
        quickSort(arr, index + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    left_index = left + 1
    right_index = right
    while left_index <= right_index:
        while left_index < len(arr) - 1 and arr[left_index] < arr[pivot]:
            left_index += 1
        while right_index > 0 and arr[right_index] > arr[pivot]:
            right_index -= 1
        if left_index < right_index:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    arr[pivot], arr[right_index] = arr[right_index], arr[pivot]
    return right_index

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











        



            











    













