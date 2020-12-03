n = int(input())
heights = list(map(int, input().split(" ")))
left = 0
right = len(heights) - 1
res = 0
while left < right:
    res = max(res, (right - left) * min(heights[left], heights[right]))
    if heights[left] >= heights[right]:
        right -= 1
    else:
        left += 1
print(res)





