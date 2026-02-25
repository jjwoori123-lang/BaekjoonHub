t = int(input())
for _ in  range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[int(1e9)] * (n+1) for _ in range(n+1)]
    sub = [0] * (n+1)
    for i in range(1, n+1):sub[i] = sub[i-1] + arr[i]
    dp = [[int(1e9)] * (n+1) for _ in range(n+1)]
    for i in range(n+1): dp[i][i] = 0 
    for length in range(2, n+1):
        for i in range(n-length+1):
            for j in range(i, i+length-1):
                dp[i][i+length-1] = min(dp[i][i+length-1], dp[i][j] + dp[j+1][i+length-1] + sub[i+length]- sub[i])
    print(dp[0][n-1])

