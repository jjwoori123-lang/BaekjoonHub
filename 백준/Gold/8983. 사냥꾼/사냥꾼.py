def cal_dist(x,x1,y1):
    return abs(x-x1) + y1
n,m,l = map(int, input().split())
gun = list(map(int, input().split()))
deer = []
for _ in range(m):deer.append(list(map(int, input().split())))
cnt = 0
for i, j in deer:
    a,b = 0, len(gun)-1
    while a<=b:
        mid = (a+b)//2
        if cal_dist(gun[mid], i,j) <= l:
            cnt+=1
            break
        elif gun[mid]- i + j > l:
            b = mid-1
        else:
            a = mid+1
print(cnt)
