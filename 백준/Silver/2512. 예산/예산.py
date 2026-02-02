n = int(input())
arr = list(map(int, input().split()))
target = int(input())

l,r = 0, max(arr)+1

while l<r:
    m = (l+r)//2
    temp = 0
    for a in arr:
        if a < m:
            temp+=a
        else:
            temp+=m
    if temp> target:
        r = m
    else:
        l = m+1
print(l-1)