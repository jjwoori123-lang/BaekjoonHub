def dfs(x, num):
    visit[x] = 1
    if x == b:
        return num
    for nx in graph[x]:
        if not visit[nx]:
            re = dfs(nx, num+1)
            if re != None:
                return re
    return None
n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
res = dfs(a, 0)
print(res) if res != None else print(-1)