from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_num(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
            return cnt

        if not wordList or len(wordList) == 0 or endWord not in wordList:
            return 0
        length = len(endWord)
        queue = deque([])
        visited = [False for _ in range(len(wordList))]
        queue.append(endWord)
        res = 1
        while queue:
            length = len(queue)
            for i in range(length):
                word = queue.popleft()
                visited[wordList.index(word)] = True
                if word == beginWord:
                    return res
                if diff_num(word, beginWord) == 1:
                    return res + 1
                for i, w in enumerate(wordList):
                    if diff_num(w, word) == 1 and not visited[i]:
                        queue.append(w)
            res += 1
        return 0


