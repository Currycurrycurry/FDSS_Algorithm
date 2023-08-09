# 定义地图大小
MAP_SIZE =16

# 初始化地图状态
map_state = [[0 for i in range(MAP_SIZE)] for j in range(MAP_SIZE)]

# 初始化坦克状态
tanks_state = {
 'D': {'x':0, 'y':0, 'dir': 'R'},
 'W': {'x': MAP_SIZE-1, 'y': MAP_SIZE-1, 'dir': 'L'}
}

# 移动
def move(tank, cmd):
    if cmd == 'U':
        if tank['dir'] == 'U' and tank['x'] >0 and map_state[tank['x']-1][tank['y']] !=1:
            tank['x'] -=1
            tank['dir'] = 'U'
    elif cmd == 'D':
        if tank['dir'] == 'D' and tank['x'] < MAP_SIZE-1 and map_state[tank['x']+1][tank['y']] !=1:
            tank['x'] +=1
            tank['dir'] = 'D'
    elif cmd == 'L':
        if tank['dir'] == 'L' and tank['y'] >0 and map_state[tank['x']][tank['y']-1] !=1:
            tank['y'] -=1
            tank['dir'] = 'L'
    elif cmd == 'R':
        if tank['dir'] == 'R' and tank['y'] < MAP_SIZE-1 and map_state[tank['x']][tank['y']+1] !=1:
            tank['y'] +=1
            tank['dir'] = 'R'

# 开火
def fire(tank):
    if tank['dir'] == 'U':
        for i in range(tank['x']-1, -1, -1):
            if map_state[i][tank['y']] ==1:
                map_state[i][tank['y']] =0
        return True
    elif tank['dir'] == 'D':
        for i in range(tank['x']+1, MAP_SIZE):
            if map_state[i][tank['y']] ==1:
                map_state[i][tank['y']] =0
        return True
    elif tank['dir'] == 'L':
        for j in range(tank['y']-1, -1, -1):
            if map_state[tank['x']][j] ==1:
                map_state[tank['x']][j] =0
        return True
    elif tank['dir'] == 'R':
        for j in range(tank['y']+1, MAP_SIZE):
            if map_state[tank['x']][j] ==1:
                map_state[tank['x']][j] =0
        return True
    return False

# 计算游戏结果
def get_result():
 D_cnt =0
 W_cnt =0
 for i in range(MAP_SIZE):
    for j in range(MAP_SIZE):
        if map_state[i][j] == 1:
            if i <= MAP_SIZE/2 and j <= MAP_SIZE/2:
                D_cnt +=1
            else:
                W_cnt +=1
            if D_cnt > W_cnt:
                return 'D'
            elif W_cnt > D_cnt:
                return 'W'
        else:
            return 'DRAW'

# 使用示例
def play_game(str_D, str_W):
 for i in range(256):
 # D 先行动
 cmd_D = str_D[i]
 move(tanks_state['D'], cmd_D)
 if cmd_D == 'F':
 if fire(tanks_state['D']):
 return 'D'
 # W 再行动
 cmd_W = str_W[i]
 move(tanks_state['W'], cmd_W)
 if cmd_W == 'F':
 if fire(tanks_state['W']):
 return 'W'
 return get_result()

# 测试
if __name__ == '__main__':
 str_D = 'R'*100 + 'F'*10 + 'R'*100 + 'F'*10 + 'D'*10 + 'L'*10 + 'F'*10 + 'U'*10
 str_W = 'L'*100 + 'F'*10 + 'L'*100 + 'F'*10 + 'U'*10 + 'R'*10 + 'F'*10 + 'D'*10
 result = play_game(str_D, str_W)
 print(result)