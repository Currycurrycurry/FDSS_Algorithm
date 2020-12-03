R, C = list(map(int, input().split(" ")))
map = []
for i in range(R):
    col = input().split("")
    map.append(col)
for r in range(R):
    for c in range(C):
        if map[r][c] != '#':
            
