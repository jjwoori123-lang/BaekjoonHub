n,m = map(int, input().split())
list_a = list(map(int, input().split()))
list_a.sort()
l,r = 0, max(list_a)
while l<r:
    cnt = 0
    mid = (l+r)//2
    for x in list_a:
        if x > mid:
            cnt += x- mid
    if cnt < m:
        r = mid
    else:
        l = mid + 1
print(l-1)
