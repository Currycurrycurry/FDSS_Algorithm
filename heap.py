import heapq
import collections

# 767 重构字符串
def reorganizeString(self, S: str) -> str:
    if len(S) < 2:
        return S
    length = len(S)
    counts = collections.Counter(S)
    print(counts)
    maxCount = max(counts.items(), key=lambda x: x[1])[1]
    if maxCount > (length + 1) // 2:
        return ""
    
    queue = [(-x[1], x[0]) for x in counts.items()]
    print(queue)
    heapq.heapify(queue)
    ans = list()

    while len(queue) > 1:
        _, letter1 = heapq.heappop(queue)
        _, letter2 = heapq.heappop(queue)
        ans.extend([letter1, letter2])
        counts[letter1] -= 1
        counts[letter2] -= 1
        if counts[letter1] > 0:
            heapq.heappush(queue, (-counts[letter1], letter1))
        if counts[letter2] > 0:
            heapq.heappush(queue, (-counts[letter2], letter2))
    if queue:
        ans.append(queue[0][1])
    
    return "".join(ans)

# 621. 任务调度器
def leastInterval(self, tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    print(counter)
    _, max_value = max(counter.items(), key=lambda x: x[1])
    print(max_value)
    max_diff_cnt = list(counter.values()).count(max_value)
    print(max_diff_cnt)
    length = (max_value - 1) * (n + 1) + max_diff_cnt
    return length if length > len(tasks) else len(tasks)
