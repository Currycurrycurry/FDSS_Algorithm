class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        _, max_value = max(counter.items(), key=lambda x: x[1])
        max_diff_cnt = list(counter.values()).count(max_value)
        length = (max_value - 1) * (n + 1) + max_diff_cnt
        return length if length > len(tasks) else len(tasks)