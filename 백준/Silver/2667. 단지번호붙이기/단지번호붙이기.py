from collections import deque
dr = [0,0,-1,1]
dc = [-1,1,0,0]
def bfs(x, y):
    ccnt = 1
    visit[x][y] = 1
    q = deque()
    q.append([x,y])
    while q:
        r,c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr< n and 0<=nc< n and arr[nr][nc] == '1' and not visit[nr][nc]:
                visit[nr][nc] = 1
                q.append([nr, nc])
                ccnt+=1
    return ccnt

n = int(input())
arr = [input() for _ in range(n)]
visit = [[0] * n for _ in range(n)]
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visit[i][j]:
            res.append(bfs(i,j))
            cnt+=1
print(cnt)
res.sort()
for r in res:
    print(r)