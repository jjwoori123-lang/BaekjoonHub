n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = int(1e9)
for i in range(n-1):
    l = i+1
    r = n-1
    while l<r:
        curr_sum = arr[i] + arr[l] + arr[r]
        if curr_sum - m <=  0:
            res = min(m - curr_sum, res)
            l+=1
        else:
            r-=1
print(m - res)