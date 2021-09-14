# my solution
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        points = [-1 for _ in range(len(dictionary))]
        for i in range(len(s)):
            for j in range(len(dictionary)):
                if points[j] < len(dictionary[j]) - 1 and dictionary[j][points[j] + 1] == s[i]:
                    points[j] += 1
        max_len = 0
        max_word = 'zzzzz'
        for i in range(len(dictionary)):
            if len(dictionary[i]) == points[i] + 1:
                if len(dictionary[i]) > max_len \
                or (len(dictionary[i]) == max_len and dictionary[i] < max_word):
                    max_word = dictionary[i]
                    max_len = len(dictionary[i])
        if max_word == 'zzzzz':
            return ''
        return max_word
        