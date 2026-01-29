def check(x,y, n):
    col = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y + n):
            if col != arr[i][j]:
                check(x,y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                return
    if col == 0:res[0]+=1
    else:res[1]+=1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [0,0]
check(0,0,n)
print(res[0])
print(res[1])