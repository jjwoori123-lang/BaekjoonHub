import sys
input = sys.stdin.readline
def cal_dist(x,x1,y1):
    return abs(x-x1) + y1
n,m,l = map(int, input().split())
gun = list(map(int, input().split()))
gun.sort()
deer = []
for _ in range(m):deer.append(list(map(int, input().split())))
cnt = 0
for i, j in deer:
    a,b = 0, len(gun)-1
    if j>l: continue
    while a<=b:
        mid = (a+b)//2
        if gun[mid] > i + l - j:
            b = mid-1
        elif gun[mid] < i - l + j:
            a = mid+1
        else:
            cnt+=1
            break
print(cnt)