def dfs(x):
    visit[x] = 1
    for nx in graph[x]:
        if not visit[nx]:
            dfs(nx)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
m = int(input())

for _ in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
print(sum(visit) - 1)