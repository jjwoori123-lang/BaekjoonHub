n = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
board = [[0]*101 for _ in range(101)]

for _ in range(n):
    y,x,d,g = map(int, input().split())
    curve = [d]
    board[x][y] = 1
    for _ in range(g):
        for i in range(len(curve)-1, -1, -1):
            curve.append((curve[i]+1) % 4)
    for i in range(len(curve)):
        x,y = x+dx[curve[i]], y+dy[curve[i]]
        board[x][y] = 1
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            result+=1
print(result)