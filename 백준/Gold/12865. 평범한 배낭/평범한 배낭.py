n,m = map(int, input().split()) #물건 갯수, 무게 제한
etc = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (m+1)
for w,v in etc:
    for i in range(m, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp[m])