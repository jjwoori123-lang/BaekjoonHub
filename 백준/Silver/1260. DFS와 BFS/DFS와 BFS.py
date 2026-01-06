from collections import deque
import copy
def dfs(x):
    print(x, end = " ")
    for i in range(1, n+1):
        if not visit[i] and arr[x][i]:
            visit[i] = 1
            dfs(i)

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        print(x, end = " ")
        for nx in range(1, n+1):
            if not visit2[nx] and arr[x][nx]:
                visit2[nx] = 1
                q.append(nx)

n,m,s = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1
visit = [0] * (n+1)
visit[s] = 1
visit2 = copy.deepcopy(visit)
dfs(s)
print()
bfs(s)