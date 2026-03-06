n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
bliz = []
dir = [(-1,0), (1,0), (0,-1), (0,1)]
for _ in range(m):
    a,b = map(int, input().split())
    bliz.append((a-1,b))
sx,sy = int(n//2), int(n//2)
tornado = []

#좌하우상
def rotate():
    dir2 = [(0,-1), (1,0), (0,1), (-1,0)]
    s = 0
    x = sx
    y = sy
    while True:
        for i in range(4):
            if i % 2 == 0:
                s +=1
            for _ in range(s):
                x+= dir2[i][0]
                y+= dir2[i][1]
                tornado.append([x,y])
                if x == 0 and y == 0: return 
def bomd(s,d):
    x,y = sx,sy
    for _ in range(s):
        x += dir[d][0]
        y += dir[d][1]
        if 0<=x<n and 0<=y < n:grid[x][y] = 0

def move_beads():
    temp = []
    for tx, ty in tornado:
        if grid[tx][ty]:temp.append(grid[tx][ty])
    for tx, ty in tornado:
        grid[tx][ty] = 0
    for i in range(len(temp)):
        tx,ty = tornado[i]
        grid[tx][ty] = temp[i]

bomb_count = [0,0,0,0]

def bomb_bead():
    beads = []
    bombed = False
    for tx, ty in tornado:
        if grid[tx][ty]:beads.append(grid[tx][ty])

    if not beads:return False
    
    new_beads = []
    i = 0
    while i< len(beads):
        target = beads[i]
        cnt = 0
        j = i
        while j< len(beads) and beads[j] == target:
            cnt +=1
            j+=1
        
        if cnt >=4:
            bomb_count[target] += cnt
            bombed = True
        else:
            for _ in range(cnt):new_beads.append(target)
        i = j
    
    for tx, ty in tornado:grid[tx][ty] = 0
    for idx in range(len(new_beads)):
        tx, ty = tornado[idx]
        grid[tx][ty] = new_beads[idx]

    return bombed 

def change_beads():
    beads = []
    for tx, ty in tornado:
        if grid[tx][ty]:
            beads.append(grid[tx][ty])
    
    if not beads: return

    new_beads = []
    i = 0
    while i < len(beads):
        target = beads[i]
        cnt = 0
        j = i
        while j < len(beads) and beads[j] == target:
            cnt += 1
            j += 1
        
        new_beads.append(cnt)
        new_beads.append(target)
        i = j
    
    for tx, ty in tornado: grid[tx][ty] = 0
    for idx in range(min(len(new_beads), n*n - 1)):
        tx, ty = tornado[idx]
        grid[tx][ty] = new_beads[idx]

rotate() 
for d, s in bliz:
    bomd(s, d)
    move_beads()
    while True:
        if not bomb_bead():break
    change_beads()
ans = bomb_count[1] * 1 + bomb_count[2] * 2 + bomb_count[3] * 3
print(ans)