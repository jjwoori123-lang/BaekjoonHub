n,m = map(int, input().split())

def get_dist(chick):
    total_dist = 0

    for x,y in city:
        min_df = float('inf')  
        for cx, cy in chick:
            dist = abs(x-cx) + abs(y-cy)
            min_df = min(min_df, dist)
        total_dist += min_df
    return total_dist


def dfs(idx, cnt):
    global ans

    if cnt == m:
        selected = [chick[i] for i in range(len(chick)) if visit[i]]
        ans = min(ans, get_dist(selected))
        return
    if idx == len(chick):
        return
    visit[idx] = True
    dfs(idx+1, cnt+1)

    visit[idx] = False
    dfs(idx+1, cnt)

arr = [list(map(int, input().split())) for _ in range(n)]
chick = list()
city = list()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chick.append([i,j])
        if arr[i][j] == 1:
            city.append([i,j])

ans = float('inf')
visit = [False] * len(chick)
dfs(0,0)
print(ans)