def dfs(x):
    #6이 들어옴, 그러면, v를 고려해서 d[x] = d[x-v] + d[v] 를 하면 된다.
    for v in val:
        dp[x] = min(dp[x], dp[x-v] + dp[v])

n = int(input())
dp = [int(1e9) for _ in range(5000+1)]
val  = [5, 3]
for v in val:
    dp[v] = 1 #3과 5의 경우는 무조건 그 값을 가져오는게 이득이다.

s = max(val)

for i in range(s+1, n+1):
    dfs(i)

print(dp[n]) if dp[n] != int(1e9) else print(-1)

