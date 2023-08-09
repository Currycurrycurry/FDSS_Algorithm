from collections import Counter

# 659. 分割数组为连续子序列
def isPossible(nums) -> bool:
    freq = Counter(nums) # 统计nums中元素的频率
    need = [0 for _ in range(max(nums)+3)]
    for num in nums:
        # 已经被用到其他顺子中
        if freq[num] == 0:
            continue
        # 判断是否能接到之前的顺子中
        if need[num] > 0:
            freq[num] -= 1
            need[num] -= 1 # 对num的需求-1
            need[num + 1] += 1 # 对num+1的需求+1
        # 作为开头新建一个顺子
        elif freq[num] > 0 and freq[num+1] > 0 and freq[num+2] > 0:
            freq[num] -= 1
            freq[num+1] -= 1
            freq[num+2] -= 1
            need[num+3] += 1 # 对num+3的需求+1
        else:
            return False
    return True