t = int(input())
for _ in range(t):
    a = int(input())
    dp = [0] * (a+1)
    if a == 1:        print(1)
    elif a == 2:        print(2)
    elif a == 3:        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, a+1):
            dp[i] =  dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[-1])