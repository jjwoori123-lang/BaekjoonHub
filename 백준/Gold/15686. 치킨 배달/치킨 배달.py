n,m = map(int, input().split())

def get_dist(s):
    tot_dist = 0

    for x,y in city:
        min_df = float('inf')
        for r,c in s:
            min_df = min(min_df, abs(r-x) + abs(y-c))
        tot_dist+= min_df
    return tot_dist

def dfs(idx, cnt):
    global ans
    if cnt == m:
        select = [chick[i] for i in range(len(chick)) if visit[i]]
        ans = min(ans, get_dist(select))
        return
    
    if idx == len(chick): return
    
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