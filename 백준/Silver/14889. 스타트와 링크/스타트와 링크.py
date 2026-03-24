def dfs(num, level):
    global res
    if level == n//2:
        a, b = 0,0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j] and i!=j:
                    a+= arr[i][j]
                elif not visit[i] and not visit[j] and i!=j:
                    b+= arr[i][j]
        res = min(abs(a-b), res)
        return
    for i in range(num, n):
        if visit[i] == 0:
            visit[i] = 1
            dfs(i+1, level+1)
            visit[i] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
res = float('inf')
dfs(0,0)
print(res)