from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash_set = defaultdict(int)
        for domino in dominoes:
            domino.sort()
            hash_set[domino[0] * 10 + domino[1]] += 1
        return sum(v * (v - 1) // 2 for v in hash_set.values())

