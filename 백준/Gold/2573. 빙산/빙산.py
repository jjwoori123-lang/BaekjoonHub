import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if arr[nx][ny] > 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 빙산 위치 초기화
icebergs = []
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            icebergs.append((i, j))

time = 0
while icebergs:
    visit = [[0] * m for _ in range(n)]
    melt_list = []
    
    # 1. 덩어리 개수 체크 (빙산 좌표 리스트만 사용)
    cnt = 0
    for r, c in icebergs:
        if not visit[r][c]:
            bfs(r, c)
            cnt += 1
        if cnt > 1: break # 2개 이상이면 즉시 중단 (시간 절약)

    if cnt >= 2:
        print(time)
        sys.exit()

    # 2. 녹일 양 계산 (빙산 좌표 리스트만 사용)
    survived = []
    for r, c in icebergs:
        sea = 0
        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0:
                sea += 1
        if sea > 0:
            melt_list.append((r, c, sea))
    
    # 3. 실제로 녹이기
    for r, c, amt in melt_list:
        arr[r][c] = max(0, arr[r][c] - amt)
    
    # 4. 살아남은 빙산만 업데이트
    icebergs = [(r, c) for r, c in icebergs if arr[r][c] > 0]
    time += 1

print(0) # 끝내 분리되지 않고 다 녹은 경우