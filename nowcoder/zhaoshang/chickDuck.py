'''
农场有n只鸡鸭排为一个队伍，鸡用“C”表示，鸭用“D”表示。当鸡鸭挨着时会产生矛盾。需要对所排的队伍进行调整，使鸡鸭各在一边。每次调整只能让相邻的鸡和鸭交换位置，现在需要尽快完成队伍调整，你需要计算出最少需要调整多少次可以让上述情况最少。例如：CCDCC->CCCDC->CCCCD这样就能使之前的两处鸡鸭相邻变为一处鸡鸭相邻，需要调整队形两次。
'''
# 最少次数的冒泡排序
def minSwap(arr):
    arr = list(arr)
    cnt = 0
    for i in range(len(arr)):
        tmp_cnt = 0
        for j in range(len(arr) - i - 1):
            if arr[j] == 'D' and arr[j+1] == 'C':
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
                tmp_cnt += 1
        if tmp_cnt == 0:
            break
    return cnt

# arr = input()
arr = 'CCCDDDCDCD'
print(minSwap(arr))


            
            