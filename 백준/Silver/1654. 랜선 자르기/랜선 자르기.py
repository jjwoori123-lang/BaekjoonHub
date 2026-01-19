n, m =map(int, input().split())
arr = [int(input()) for _ in range(n)]
l,r = 1, max(arr)+1
while l<r:
    mid = (l+r)//2
    cnt = 0
    for a in arr:
        cnt += a // mid
    if cnt < m:
        r = mid
    else:
        l = mid + 1
print(l-1)