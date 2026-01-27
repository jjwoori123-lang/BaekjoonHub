from collections import deque

def bfs(x):
    q = deque([x])
    visit[x] = 1
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visit[nx] == 0:
                visit[nx] = 1
                dist[nx] = dist[x] + 1
                q.append(nx)

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

dist = [0] * (n+1)
visit = [0] * (n+1)
bfs(x)
cnt = 0
for i in range(n+1):
    if dist[i] == k:
        cnt+=1
        print(i)
if cnt ==0:
    print(-1)