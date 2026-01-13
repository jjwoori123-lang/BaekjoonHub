n = int(input())
tot = n**2
graph = [[ ] for _ in range(tot+1)]
arr = [[0] * n for _ in range(n)]
order = []
for _ in range(tot):
    a,*b = map(int, input().split())
    graph[a] = b
    order.append(a)

dx = [0,0,-1,1]
dy = [-1,1,0,0]
for o in order:
    cand = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                continue
            
            empty_cnt = 0
            fill_cnt = 0
    
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if arr[nx][ny] in graph[o]: fill_cnt+=1
                    elif arr[nx][ny] == 0: empty_cnt+=1
            cand.append((-fill_cnt, -empty_cnt, i,j))
    cand.sort()
    x,y = cand[0][2], cand[0][3]
    arr[x][y] = o

res = 0
for i in range(n):
    for j in range(n):
         tmp = 0 
         for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] in graph[arr[i][j]]: tmp+=1
         if tmp: res += 10**(tmp-1)
print(res)