def dfs(x):
    visit[x] = 1
    for nx in graph[x]:
        if visit[nx] == 0:
            dfs(nx)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        cnt+=1
print(cnt)