import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * m for _ in range(n)]

f = int(input())
# wall_r[r][c] : (r, c)의 오른쪽에 벽이 있으면 True
wall_r = [[False] * m for _ in range(n)]
# wall_u[r][c] : (r, c)의 위쪽에 벽이 있으면 True
wall_u = [[False] * m for _ in range(n)]

for _ in range(f):
    x, y, t = map(int, input().split())
    if t == 1: # 오른쪽
        wall_r[x-1][y-1] = True
    else: # 위쪽
        wall_u[x-1][y-1] = True

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 온풍기 위치 미리 저장
fans = []
for i in range(n):
    for j in range(m):
        if 1 <= pan[i][j] <= 4:
            fans.append((i, j, pan[i][j]))

def air():
    total_added = [[0] * m for _ in range(n)]
    for x, y, d in fans:
        tmp = [[0] * m for _ in range(n)]
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < n and 0 <= ny < m): continue
        
        tmp[nx][ny] = 5
        q = deque([(nx, ny, 5)])
        
        while q:
            qx, qy, val = q.popleft()
            if val == 0: break

            # d=1:우, 2:좌, 3:상, 4:하
            if d == 1: # 오른쪽 확산
                # 우상 (위로 가서 오른쪽)
                if qx-1 >= 0 and qy+1 < m and not wall_u[qx][qy] and not wall_r[qx-1][qy] and not tmp[qx-1][qy+1]:
                    tmp[qx-1][qy+1] = val - 1
                    q.append((qx-1, qy+1, val - 1))
                # 우 (오른쪽)
                if qy+1 < m and not wall_r[qx][qy] and not tmp[qx][qy+1]:
                    tmp[qx][qy+1] = val - 1
                    q.append((qx, qy+1, val - 1))
                # 우하 (아래로 가서 오른쪽)
                if qx+1 < n and qy+1 < m and not wall_u[qx+1][qy] and not wall_r[qx+1][qy] and not tmp[qx+1][qy+1]:
                    tmp[qx+1][qy+1] = val - 1
                    q.append((qx+1, qy+1, val - 1))
            
            elif d == 2: # 왼쪽 확산
                if qx-1 >= 0 and qy-1 >= 0 and not wall_u[qx][qy] and not wall_r[qx-1][qy-1] and not tmp[qx-1][qy-1]:
                    tmp[qx-1][qy-1] = val - 1
                    q.append((qx-1, qy-1, val - 1))
                if qy-1 >= 0 and not wall_r[qx][qy-1] and not tmp[qx][qy-1]:
                    tmp[qx][qy-1] = val - 1
                    q.append((qx, qy-1, val - 1))
                if qx+1 < n and qy-1 >= 0 and not wall_u[qx+1][qy] and not wall_r[qx+1][qy-1] and not tmp[qx+1][qy-1]:
                    tmp[qx+1][qy-1] = val - 1
                    q.append((qx+1, qy-1, val - 1))
                    
            elif d == 3: # 위쪽 확산
                if qx-1 >= 0 and qy-1 >= 0 and not wall_r[qx][qy-1] and not wall_u[qx][qy-1] and not tmp[qx-1][qy-1]:
                    tmp[qx-1][qy-1] = val - 1
                    q.append((qx-1, qy-1, val - 1))
                if qx-1 >= 0 and not wall_u[qx][qy] and not tmp[qx-1][qy]:
                    tmp[qx-1][qy] = val - 1
                    q.append((qx-1, qy, val - 1))
                if qx-1 >= 0 and qy+1 < m and not wall_r[qx][qy] and not wall_u[qx][qy+1] and not tmp[qx-1][qy+1]:
                    tmp[qx-1][qy+1] = val - 1
                    q.append((qx-1, qy+1, val - 1))
                    
            elif d == 4: # 아래쪽 확산
                if qx+1 < n and qy-1 >= 0 and not wall_r[qx][qy-1] and not wall_u[qx+1][qy-1] and not tmp[qx+1][qy-1]:
                    tmp[qx+1][qy-1] = val - 1
                    q.append((qx+1, qy-1, val - 1))
                if qx+1 < n and not wall_u[qx+1][qy] and not tmp[qx+1][qy]:
                    tmp[qx+1][qy] = val - 1
                    q.append((qx+1, qy, val - 1))
                if qx+1 < n and qy+1 < m and not wall_r[qx][qy] and not wall_u[qx+1][qy+1] and not tmp[qx+1][qy+1]:
                    tmp[qx+1][qy+1] = val - 1
                    q.append((qx+1, qy+1, val - 1))

        for i in range(n):
            for j in range(m):
                total_added[i][j] += tmp[i][j]
    
    for i in range(n):
        for j in range(m):
            arr[i][j] += total_added[i][j]

def adjust():
    diff = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            # 오른쪽 체크
            if c+1 < m and not wall_r[r][c]:
                val = abs(arr[r][c] - arr[r][c+1]) // 4
                if arr[r][c] > arr[r][c+1]:
                    diff[r][c] -= val
                    diff[r][c+1] += val
                else:
                    diff[r][c] += val
                    diff[r][c+1] -= val
            # 아래쪽 체크
            if r+1 < n and not wall_u[r+1][c]:
                val = abs(arr[r][c] - arr[r+1][c]) // 4
                if arr[r][c] > arr[r+1][c]:
                    diff[r][c] -= val
                    diff[r+1][c] += val
                else:
                    diff[r][c] += val
                    diff[r+1][c] -= val
    for i in range(n):
        for j in range(m):
            arr[i][j] += diff[i][j]

def cool():
    for r in range(n):
        for c in range(m):
            if r == 0 or r == n-1 or c == 0 or c == m-1:
                if arr[r][c] > 0:
                    arr[r][c] -= 1

def check():
    for i in range(n):
        for j in range(m):
            if pan[i][j] == 5:
                if arr[i][j] < k: return False
    return True

choco = 0
while choco <= 100:
    air()
    adjust()
    cool()
    choco += 1
    if check(): break

print(choco)