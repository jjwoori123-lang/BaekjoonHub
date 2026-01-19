import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dp = [0] * (1000001)
val = [int(input()) for i in range(n)]
for v in val:
    dp[v] = 1

for i in range(1, m+1):
    for v in val:
        if (i+v) <= m and dp[i]: 
            if not dp[i+v] :
                dp[i+v] = dp[i] + 1
            elif dp[i+v] > 0:
                dp[i+v] = min(dp[i+v], dp[i]+ 1)
if dp[m] == 0:
    print(-1)
else:
    print(dp[m])

