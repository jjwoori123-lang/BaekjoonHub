import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list()
for _ in range(n): arr.append(int(input()))
arr.sort()
res = 0
l,r = 1, arr[-1]  - arr[0]
while l <= r:
    mid = (l+r+1)//2
    cur = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i] >= mid + cur:
            cnt+=1
            cur = arr[i]
    if cnt  >= m:
        l = mid + 1
    else:
        r = mid - 1
print(r)