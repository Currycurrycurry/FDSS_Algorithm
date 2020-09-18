def majorityElement(nums):
    num_cnt_dict = dict()
    for num in nums:
        if num_cnt_dict.get(num) is not None:
            num_cnt_dict[num] += 1
        else:
            num_cnt_dict[num] = 1
    item_val = -float('inf')
    key_val = 0
    # print(num_cnt_dict.keys())
    for key, value in num_cnt_dict.items():
        if value > item_val:
            key_val = key
            item_val = value
    return key_val


def majorityElement2(nums):
    return sorted(nums)[len(nums)//2]

def majorityElement3(nums):
    votes = 0
    for num in nums:
        if votes == 0:
            x = num
        if x == num:
            votes += 1
        else:
            votes -= 1
    return x

def majorityElement4(nums):
    return collections.Counter(nums).most_common(1)[0][0]

