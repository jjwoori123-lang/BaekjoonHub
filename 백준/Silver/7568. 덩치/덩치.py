n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
level = [0] * n
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j: continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
           rank+=1
        level[i] = rank
print(*level)
