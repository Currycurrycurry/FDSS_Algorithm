class Solution:
    def sortString(self, s: str) -> str:
        chars = [0 for _ in range(26)]
        for letter in s:
            chars[ord(letter) - ord('a')] += 1
        res = []
        while any(chars):
            for i in range(len(chars)):
                if chars[i] != 0:
                    chars[i] -= 1
                    res.append(chr(i+ord('a')))
            for i in range(len(chars)-1, -1, -1):
                if chars[i] != 0:
                    chars[i] -= 1
                    res.append(chr(i+ord('a')))
        return ''.join(res)

        