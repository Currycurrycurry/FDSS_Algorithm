import sys
s = sys.stdin.readline().strip()
print(s)
res = 0
s = list(s)
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        res += 1
        s[i] = 10
    else:
        continue
print(res)