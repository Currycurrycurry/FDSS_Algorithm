def getHighestScore():
    pass

N, M = list(map(int, input().split(' ')))
scores = list(map(int, input().split(' ')))
ans = []
for _ in range(M):
    tmp = input().split(' ')
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    if tmp[0] == 'Q':
        if tmp[1] < tmp[2]:
            ans.append(max(scores[tmp[1] - 1: tmp[2]]))
        else:
            ans.append(max(scores[tmp[2] - 1: tmp[1]]))
    elif tmp[0] == 'U':
        scores[tmp[1] - 1] = tmp[2]

for i in ans:
    print(i)