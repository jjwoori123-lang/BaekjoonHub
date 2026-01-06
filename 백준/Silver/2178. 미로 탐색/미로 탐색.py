from collections import deque
def bfs(x,y):
    q = deque()
    visit[x][y] = 1
    q.append([x,y])
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            print(arr[x][y])
            return
        for nx, ny in ([x+1, y], [x-1, y], [x, y+1], [x, y-1]):
            if 0<=nx<n and 0<=ny< m:
                if visit[nx][ny] == 0 and arr[nx][ny]:
                    arr[nx][ny] += arr[x][y]
                    q.append([nx, ny])
                    visit[nx][ny] = 1
        

n,m = map(int, input().split())
arr = [[int(i) for i in input().strip()] for _ in range(n)]
visit = [[0] * m for _ in range(n)]
bfs(0,0)
