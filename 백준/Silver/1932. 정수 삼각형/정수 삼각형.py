n = int(input())
arr = [[0] * n for _ in range(n)]
dp = list([0] * i for i in range(1, n+1))
for i in range(n):
    arr[i] = list(map(int, input().split()))

dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + arr[i][j])
        elif j == i:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i][j])
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])
print(max(dp[n-1]))