from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** n)]
lev = list(map(int, input().split()))

def rotate_grid(l):
    new_grid = [[0] * (2 ** n) for _ in range(2**n)]
    for r in range(0, 2**n, 2**l):
        for c in range(0, 2**n, 2**l):
            for i in range(0, 2**l):
                for j in range(0, 2**l):
                    new_grid[r+j][c+2**l-1-i] = arr[r+i][c+j]
    return new_grid

def melt_ice():
    melt = []

    for i in range(2**n):
        for j in range(2**n):
            if not arr[i][j]: continue

            cnt = 0

            for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
                nx, ny = i+dx, j+dy
                if 0<=nx<2**n and 0<=ny<2**n:
                    if arr[nx][ny]: cnt+=1

            if cnt < 3:melt.append((i,j))
    for i,j in melt:
        arr[i][j]-=1

def cnt_ice():
    visit = [[0] * (2**n) for _ in range(2**n)]
    max_cnt = 0

    for i in range(2**n):
        for j in range(2**n):
            if arr[i][j] and not visit[i][j]:
                q = deque([(i,j)])
                visit[i][j]  = 1
                cur_cnt = 0
                while q:
                    x,y = q.popleft()
                    cur_cnt+=1
                    for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<2**n and 0<=ny<2**n:
                            if arr[nx][ny] and not visit[nx][ny]:
                                visit[nx][ny] = 1
                                q.append((nx, ny))
                    max_cnt = max(max_cnt, cur_cnt)
    return max_cnt
for i in range(m):
    arr = rotate_grid(lev[i])
    melt_ice()

res = cnt_ice()
goal = 0
for i in range(2**n):
    for j in range(2**n):
        if arr[i][j]:
            goal += arr[i][j]
print(goal)
if res == 0:
    print(0)
else:
    print(res)