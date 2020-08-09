# 1
def sortAndSearch(nums):
    nums = sorted(nums)
    duplicates = []
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            duplicates.append(nums[i])
            i += 1
    return duplicates

nums = [2,3,1,0,2,5,3]
print(sortAndSearch(nums))

# 2
def hashSearch(nums):
    duplicates, tmp_set = set(), set()
    for num in nums:
        if num in tmp_set:
            duplicates.add(num)
        else:
            tmp_set.add(num)
    return duplicates

nums = [2,3,1,0,0,0,5,5,5,3]
print(hashSearch(nums))

# 3
def positionIndexSearch(nums):
    for index, num in enumerate(nums):
        if index == num:
            continue
        elif nums[num] == num:
            return num
        else:
            nums[num], nums[index] = nums[index], nums[num]
    return -1

nums = [2,3,1,0,2,5,3]
print(positionIndexSearch(nums))

# 4
def bucketSearch(nums):
    if not nums:
        return -1
    bucket = [0] * len(nums)
    for num in nums:
        bucket[num] += 1
    return [index for index, value in enumerate(bucket) if value > 1]

nums = [2,3,1,0,2,5,3]
print(bucketSearch(nums))

# 5
def binarySearch(nums):
    def recursion(nums, start, end):
        def count_range(nums, start, end):
            cnt = 0
            for num in nums:
                if start <= num <= end:
                    cnt += 1
            return cnt
        if start == end: 
            return start
        mid = (start + end) // 2
        if count_range(nums, start, mid) > (mid - start + 1):
            return recursion(nums, start, mid)
        if count_range(nums, mid + 1, end) > (end - mid):
            return recursion(nums, mid + 1, end)
    return recursion(nums, 1, len(nums) - 1)

nums = [2,3,5,4,3,2,6,7]
print(binarySearch(nums))









