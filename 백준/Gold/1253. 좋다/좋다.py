n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
for i in range(n):
    target = arr[i]
    l = 0
    r = n-1
    while l<r:
        if arr[l] + arr[r] == target:
            if l!= i and r != i:
                cnt+=1
                break
            elif l== i:
                l+=1
            elif r == i:
                r-=1
        elif arr[l] + arr[r] < target:
            l+=1
        elif arr[l] + arr[r] > target:
            r-=1
print(cnt)
