# ！旋转数组的最小数字
# 双指针法
# 初始化： 用两个指针分别指向数组的第一个元素和最后一个元素（第一个元素大于/等于最后一个元素，然后用中间元素来进行判断
# 【在后面】如果该中间元素位于前面的递增子数组，那么它应该大于/等于第一个指针指向的元素，此时数组中最小的元素应该位于该中间元素的后面，
# 【在前面】如果该中间元素位于后面的递增子数组，那么它应该小雨/等于第二个指针指向的元素，此时数组中最小的元素应该位于该中间元素的前面。
# 特例：

def findMinNumWrong(nums):
    # binary search
    start = 0
    end = len(nums) - 1
    while end - start != 1:
        mid = start + (end - start) // 2
        if nums[mid] > nums[start]:
            start = mid
            continue
        if nums[mid] < nums[end]:
            end = mid
            continue
    return nums[end]

def findMinNumRight(nums):
    index1 = 0
    index2 = len(nums) - 1
    indexMid = index1
    while nums[index1] >= nums[index2]:
        if index2 - index1 == 1:
            indexMid = index2
            break
        indexMid = index1 + (index2 - index1) // 2
        if nums[indexMid] >= nums[index1]:
            index1 = indexMid
        elif nums[indexMid] <= nums[index2]:
            index2 = indexMid
    return nums[indexMid]

# 特例：具有很多重复元素
# 第一个指针、第二个指针、中间指针指向的数字都相同
# 当两个指针指向的数字及它们中间的数字相同时，我们无法判断中间的数字是位于前面的子数组还是后面的子数组，无法通过移动指针的方式缩小查找的范围。
def findMinNumTotallyRight(nums):
    def minInOrder(nums, index1, index2):
        res = nums[index1]
        for i in range(index1+1, index2+1):
            if res > nums[i]:
                res = nums[i]
        return res
    index1 = 0
    index2 = len(nums) - 1
    indexMid = index1
    while nums[index1] >= nums[index2]:
        if index2 - index1 == 1:
            indexMid = index2
            break
        indexMid = index1 + (index2 - index1) // 2
        if nums[index1] == nums[index2] and nums[indexMid] == nums[index1]:
            return minInOrder(nums, index1, index2)
        if nums[indexMid] >= nums[index1]:
            index1 = indexMid
        elif nums[indexMid] <= nums[index2]:
            index2 = indexMid
    return nums[indexMid]


nums = [5,6,7,8,1,2,3,4]
print(findMinNum(nums))