from collections import deque

def bfs(x,y,c):
    q = deque()
    q.append([x,y])
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    blk_cnt, rain_cnt= 1,0
    blk, rain = [[x,y]], []
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if arr[nx][ny] == c:
                    blk_cnt+=1
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    blk.append([nx, ny])
                if not arr[nx][ny]:
                    blk_cnt+=1
                    rain_cnt+=1
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    rain.append([nx, ny])

    for x,y in rain: visit[x][y] = 0
    return [blk_cnt, rain_cnt, blk+rain]

def gravity(arr):
    for i in range(n-2, -1, -1):
        for j in range(n):
            if arr[i][j] > -1:
                r = i
                while True:
                    if 0<=r+1<n and arr[r+1][j] == -2:
                        arr[r+1][j], arr[r][j] = arr[r][j], -2
                        r+=1
                    else: break
def remove(blk):
    for x,y in blk: arr[x][y] = -2
 
def rotate90(arr):
    new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[n-1-j][i] = arr[i][j]
    return  new

n, m = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
arr = [list(map(int, input().split())) for _ in range(n)]
score = 0
while True:
    visit = [[0] * n for _ in range(n)]
    blk = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visit[i][j]:
                visit[i][j] = 1
                blk_info =  bfs(i,j, arr[i][j])
                if blk_info[0] >=2: blk.append(blk_info)
    blk.sort(reverse=True)
    if not blk: break
    remove(blk[0][2])
    score += blk[0][0] ** 2
    gravity(arr)
    arr = rotate90(arr)
    gravity(arr)
print(score)