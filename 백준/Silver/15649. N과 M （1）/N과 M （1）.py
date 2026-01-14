def dfs():
    if len(list_a) == m:
        print(*list_a)
        return
    for i in range(1, n+1):
        if i not in list_a:
            list_a.append(i)
            dfs()
            list_a.pop()

n, m = map(int, input().split())
list_a = []
cnt = 0
dfs()