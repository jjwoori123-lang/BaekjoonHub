import copy
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
n, m = map(int, input().split())
shark_dir = {0: (0,0), 1: (-1, 0), 2: (0, -1), 3: (1,0), 4: (0, 1) }
board= [[[] for _ in range(5)]  for _ in range(5)]
smells = [[0] * 5 for _ in range(5)]
for _ in range(n):
    a,b,c = map(int, input().split())
    board[a][b].append(c)
sx, sy = map(int, input().split())

def fish_move(board):
    global smells
    new_board = [[[] for _ in range(5)]  for _ in range(5)]
    for i in range(1, 5):
        for j in range(1, 5):
            for d in board[i][j]:
                nd = d
                while True:
                    nx = i+ dx[nd]
                    ny = j+ dy[nd]
                    if nx < 1 or nx > 4 or  ny < 1 or ny > 4:
                        nd = ((nd-1) -1) % 8 + 1
                        if nd == d:
                            new_board[i][j].append(d)
                            break
                        continue
                    if smells[nx][ny] > 0:
                        nd = ((nd-1) -1) % 8 + 1
                        if nd == d:
                            new_board[i][j].append(d)
                            break
                        continue
                    if (nx, ny) == (sx, sy):
                        nd = ((nd-1) -1) % 8 + 1
                        if nd == d:
                            new_board[i][j].append(d)
                            break
                        continue
                    new_board[nx][ny].append(nd)
                    break
    return new_board

def dfs(depth, x, y, path, sum, board):
    global method 
    if depth == 3:
        method.append((sum ,path))
        return 
    for i in range(1, 5):
        nx = x + shark_dir[i][0]
        ny = y + shark_dir[i][1]
        if nx < 1 or nx > 4 or  ny < 1 or ny > 4:
            continue
        tmp = len(board[nx][ny])
        tmpcopy = board[nx][ny]
        board[nx][ny] = []
        dfs(depth+1, nx, ny, path+str(i), sum+tmp, board)
        board[nx][ny] = tmpcopy

def find_method():
    global sx, sy
    x,y = sx, sy
    new_board = copy.deepcopy(board)    
    dfs(0,x,y,"", 0, new_board)

for _ in range(m):
    method = []
    copy_board = copy.deepcopy(board)
    board = fish_move(board)
    find_method()
    method.sort(key=lambda x: (-x[0], x[1]))
    for d in method[0][1]:
        nx = sx + shark_dir[int(d)][0]
        ny = sy + shark_dir[int(d)][1]
        if len(board[nx][ny]) > 0:
            board[nx][ny] = []
            smells[nx][ny] = 3
        sx, sy = nx, ny
    for i in range(1, 5):
        for j in range(1, 5):
            if smells[i][j] > 0:
                smells[i][j] -= 1
    for i in range(1, 5):
        for j in range(1, 5):
            board[i][j] += copy_board[i][j]
answer = 0
for i in range(1, 5):
    for j in range(1, 5):
        answer += len(board[i][j])
print(answer)
