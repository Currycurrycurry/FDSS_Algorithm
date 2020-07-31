def lastStoneWeight(self, stones: List[int]) -> int:
    while len(stones) >= 2:
        max_num1 = max(stones)
        stones.remove(max_num1)
        max_num2 = max(stones)
        stones.remove(max_num2)
        if max_num1 > max_num2:
            max_num1, max_num2 = max_num2, max_num1
        if max_num2 - max_num1 > 0:
            stones.append(max_num2 - max_num1)
    if len(stones) == 0:
        return 0
    if len(stones) == 1:
        return stones[0]


        