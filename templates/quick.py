
quick_sort = lambda array: array \
if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

print(quick_sort([5,4,3,2,1]))

def quickSort(nums, start, end):
    if start > end:
        return
    key = nums[start]
    low = start + 1
    high = end
    while low < high:
        while low < high and nums[high] > key:
            high -= 1
        while low < high and nums[low] < key:
            low += 1
        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    nums[high], nums[start] = nums[start], nums[high]
    quickSort(nums, start, high - 1)
    quickSort(nums, high + 1, end)

nums = [3, 4, 5, 2, 1]
quickSort(nums, 0, len(nums) - 1)
print(nums)

def quickSort(nums, start, end):
    if start < end:
        q = partition(nums, start, end)
        quickSort(nums, start, q - 1)
        quickSort(nums, q + 1, end)

def partition(nums, start, end):
    key = nums[end]
    left_index = start - 1
    for right_index in range(start, end):
        if nums[right_index] <= key:
            left_index += 1
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
    nums[left_index + 1], nums[end] = nums[end], nums[left_index + 1]
    return left_index + 1

nums = [5,6,7,1,2]
quickSort(nums, 0, len(nums) - 1)
print(nums)

'''
迭代与递归的转换需要考虑：
（1）stack保存啥——数组的上下边界
（2）递归/迭代结束的条件是啥——left > right
'''

def quickSort(nums, left, right):
    if left >= right:
        return
    stack = [left, right]
    while stack:
        high = stack.pop()
        low = stack.pop()
        if high <= low:
            continue
        key = nums[high]
        left_index = low - 1
        for right_index in range(low, high):
            if nums[right_index] <= key:
                left_index += 1
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
        nums[left_index + 1], nums[high] = nums[high], nums[left_index + 1]
        # 注意：left_index + 1 才是partition点
        stack.extend([low, left_index, left_index + 2, high])

nums = [3, 4, 5, 2, 1]
quickSort(nums, 0, len(nums) - 1)
print(nums)