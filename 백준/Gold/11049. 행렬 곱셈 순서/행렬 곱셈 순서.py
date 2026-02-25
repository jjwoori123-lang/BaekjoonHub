n = int(input())
arr = []
for _ in range(n):
    lista  = list(map(int, input().split()))
    arr.append(lista)
dp = [[int(1e9)] * (n) for _ in range(n)]
for i in range(0, n):
    dp[i][i] = 0
for l in range(2, n+1):
    for i in range(n-l+1):
        for j in range(i, i+l-1):
            dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][j] + dp[j+1][i+l-1] + arr[i][0] * arr[j][1] * arr[i+l-1][1])
print(dp[0][n-1])