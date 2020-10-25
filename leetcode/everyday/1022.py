class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        start, end, result = 0, 0, []
        char_map = [0 for _ in range(26)]
        for i in range(len(S)):
            char_map[ord(S[i]) - ord('a')] = i
        for i in range(len(S)):
            end = max(end, char_map[ord(S[i]) - ord('a')])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result


        