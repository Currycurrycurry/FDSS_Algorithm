class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        s = set(list(A[0]))
        for a in A:
            s = set(list(a)) & s
        return list(s)


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        res = []
        for i in A[0]:
            all_has = True
            for a in A:
                if i in a:
                    continue
                else:
                    all_has = False
            if all_has:
                if i not in res:
                    res.append(i)
                else:
                    smallest_num = float('inf')
                    for a in A:
                        smallest_num = min(smallest_num, a.count(i))
                    print(smallest_num)
                    for _ in range(smallest_num - 1):
                        res.append(i)
        return res


class Solution: 
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        res = []
        l = [0 for _ in range(26)]
        for i in A[0]:
            l[ord(i) - ord('a')] += 1
        for i in range(1, len(A)):
            temp = [0 for _ in range(26)]
            for a in A[i]:
                temp[ord(a) - ord('a')] += 1
            for j in range(26):
                l[j] = min(l[j], temp[j])
        
        for i in range(len(l)):
            if l[i] > 0:
                for _ in range(l[i]):
                    res.append((chr(ord('a') + i)))
        return res

class Solution: 
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += minnum * k
        return res

class Solution: 
    def commonChars(self, A: List[str]) -> List[str]:
        return [ char for char in set(A[0]) for i in range( min(s.count(char) for s in A )) ]


class Solution: 
    def commonChars(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())