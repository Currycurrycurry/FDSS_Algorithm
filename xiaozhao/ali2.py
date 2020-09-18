n = int(input())
C = list(map(int, input().split(' ')))
graph = [[1] * n for _ in range(n)]
def getPerfectDegree(graph, C):
    C = sorted(C)
    # 爷放弃了 贵阿里再见 完全不会谢谢您嘞
print(getPerfectDegree(graph, C))