def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if 1 not in flowerbed and n <= len(flowerbed):
        return (len(flowerbed) + 1) // 2 >= n
    cnt = []
    index = 0
    tmp = 0
    while index < len(flowerbed):
        while index < len(flowerbed) and flowerbed[index] == 0:
            tmp += 1
            index += 1
        else:
            cnt.append(tmp)
            tmp = 0
            index += 1
    if flowerbed[0] == 1:
        start = 0
        val_start = 0
    else:
        start = 1
        val_start = cnt[0] // 2
    if flowerbed[-1] == 1:
        end = len(cnt)
        val_end = 0
    else:
        end = -1
        val_end = cnt[-1] // 2

    cnt_new = map(lambda x: (x-1)//2 if x > 0 else 0, cnt[start:end])
    cnt_sum = sum(list(cnt_new)) +  val_start + val_end
    return cnt_sum >= n

def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    tmp = [0] + flowerbed + [0]
    for i in range(1, len(tmp) - 1):
        if tmp[i-1] == 0 and tmp[i] == 0 and tmp[i+1] == 0:
            tmp[i] = 1
            n -= 1
    return n <= 0