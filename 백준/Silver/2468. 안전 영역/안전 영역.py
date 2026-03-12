from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y, k):
    global cnt
    q = deque()
    q.append([x,y])
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny  = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] > k and not visit[nx][ny]:
                q.append([nx, ny])
                visit[nx][ny] = cnt
def simul(k):
    global cnt
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visit[i][j]:
                cnt+=1
                bfs(i,j,k)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 1
for k in range(1, 101):
    visit = [[0] * n for _ in range(n)]
    cnt = 0
    simul(k)
    res = max(res, cnt)
print(res)
