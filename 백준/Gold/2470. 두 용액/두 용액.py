import sys
input = sys.stdin.readline
n  = int(input())
arr = list(map(int, input().split()))
arr.sort()
l,r = 0,n-1
final = [arr[l], arr[r]]
ans = abs(arr[l] + arr[r])
while l<r:
    mid = arr[l] + arr[r]
    if abs(mid) < ans:
        ans = abs(mid)
        final = [arr[l], arr[r]]
        if ans == 0:
            break
    if mid < 0:
        l+=1
    else:
        r-=1
print(final[0], final[1])