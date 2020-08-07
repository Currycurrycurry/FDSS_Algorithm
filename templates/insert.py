# basic
def insertionSort(nums):
    for i in range(len(nums)):
        current = nums[i]
        pre = i - 1
        while pre >= 0 and current < nums[pre]:
            nums[pre + 1] = nums[pre]
            pre -= 1
        nums[pre + 1] = current
    return nums

nums = [5,4,3,2,1]
print(insertionSort(nums))

def insertionSort2(nums):
    for i in range(len(nums) - 1, -1, -1):
        current = nums[i]
        pre = i + 1
        while pre <= len(nums) - 1 and current > nums[pre]:
            nums[pre - 1] = nums[pre]
            pre += 1
        nums[pre - 1] = current
    return nums

nums = [3,2,1,4,5]
print(insertionSort2(nums))

def insertionSort3(nums):
    pass




    
