n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = [(0,-1), (-1,-1), (-1,0),(-1,1), (0,1), (1,1), (1,0), (1,-1)]
move = []
for _ in range(m):
    d,s = list(map(int, input().split()))
    move.append([d-1, s])

cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

def check_diag(cloud):
    for c in cloud:
        x, y= c[0], c[1]
        cnt = 0
        for nx, ny in ((x-1,y-1),(x+1, y+1), (x-1, y+1), (x+1, y-1)):
            if 0<=ny<n and 0<=nx<n:
                if arr[nx][ny]: cnt +=1
        arr[x][y] += cnt          

def cloud_move(d, s):
    global cloud
    dx,dy = dir[d]
    new_cloud = []
    for c in cloud:
        x, y= c[0], c[1]
        nx = (x + s * dx + n) % n
        ny = (y + s * dy + n) % n
        new_cloud.append((nx, ny))
    cloud = new_cloud
    for c in cloud:
        x, y= c[0], c[1]
        arr[x][y] +=1
    check_diag(cloud)

for i in range(m):        
    cloud_move(move[i][0], move[i][1])
    c = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and (i,j) not in cloud:
                c.append((i,j))
                arr[i][j] -=2
    cloud = c    
res = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]: res += arr[i][j]
print(res)