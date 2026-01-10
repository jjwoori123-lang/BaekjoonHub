
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx< a and 0<=ny < b and arr[nx][ny] == 1 :
            arr[nx][ny] = -1
            dfs(nx, ny)
t = int(input())
for _ in range(t):
    b,a,n = map(int, input().split())
    arr = [[0] * (b) for _ in range(a)]
    for j in range(n):
        y,x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(a):
        for j in range(b):
            if arr[i][j] == 1:
                dfs(i,j)
                cnt+=1
    print(cnt)