# 小招喵喜欢吃喵粮。这里有 N 堆喵粮，第 i 堆中有 p[i] 粒喵粮。喵主人离开了，将在 H 小时后回来。

# 小招喵可以决定她吃喵粮的速度 K （单位：粒/小时）。每个小时，她将会选择一堆喵粮，从中吃掉 K 粒。如果这堆喵粮少于 K 粒，她将吃掉这堆的所有喵粮，然后这一小时内不会再吃更多的喵粮。  

# 小招喵喜欢慢慢吃，但仍然想在喵主人回来前吃掉所有的喵粮。

# 返回她可以在 H 小时内吃掉所有喵粮的最小速度 K（K 为整数）。
import math
def minSpeed(food, h):
    if h < len(food):
        return -1
    if h == len(food):
        return max(food)
    food = sorted(food)
    ans = 0
    for i in range(food[-1], 1, -1):
        tmp_sum = 0
        for j in food:
            tmp_sum += math.ceil(j / i)
        if tmp_sum <= h:
            ans = i
    return ans

food = list(map(int, input().split()))
h = int(input())
print(minSpeed(food, h))


    