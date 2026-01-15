from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
m = int(input())
for _ in range(m):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 2
k = int(input())
order = []
for _ in range(k):
    order.append(list(input().split()))

#처음에는 오른쪽으로 간다 이말이야
dx = [0,1,0,-1]
dy = [1,0,-1,0] #우하좌상
idx = 1 #1초
dir = 0
x,y = 0,0
arr[x][y] = 1 #뱀의 위치
q = deque()

q.append((x,y))
time = 0
while True:
    time +=1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0<=nx<n and 0<=ny< n and arr[nx][ny] != 1:
       if arr[nx][ny] == 2:
           arr[nx][ny] = 1
           q.append((nx, ny))
       else:
           arr[nx][ny] = 1
           q.append((nx, ny))
           tx, ty = q.popleft()
           arr[tx][ty] = 0
    else:
        break
    x,y = nx, ny
    
    if order and str(time) == order[0][0]:
        if order[0][1] == "D":
            dir = (dir +1)%4
        else:
            dir = (dir + 3) % 4
        order.pop(0)
print(time)

