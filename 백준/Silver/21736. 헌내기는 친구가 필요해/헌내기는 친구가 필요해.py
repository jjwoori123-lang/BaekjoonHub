from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    while q:
        sx, sy = q.popleft()
        for i in range(4):
            nx = sx + dx[i]
            ny = sy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] !=  'X' and not visit[nx][ny]:
                visit[nx][ny] = 1
                q.append((nx, ny))
                
                if arr[nx][ny] == 'P':
                    cnt += 1

n, m  = map(int, input().split())
arr = [input() for _ in range(n)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            sx, sy = i, j


cnt = 0
bfs(sx, sy)
print(cnt if cnt > 0 else 'TT')