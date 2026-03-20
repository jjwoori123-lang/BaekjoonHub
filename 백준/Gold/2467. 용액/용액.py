n = int(input())
arr = list(map(int, input().split()))
l, r = 0, len(arr)-1
goal = float('inf')
ans = [float('inf'), float('inf')]
while l<r:
    if abs(arr[l] + arr[r]) < goal:
        goal = abs(arr[l] + arr[r])
        ans = [arr[l], arr[r]]

    if arr[l] + arr[r] < 0:l+=1
    else: r-=1
print(*ans)