target = int(input())
dp = [float('inf')] * (target+1)
s = 1
dp[s] = 0
for i in range(1, target+1):
    for nx in [i+1, i*2, i*3]:
        if dp[i] != float('inf') and nx < target+1:
            dp[nx] = min(dp[nx], dp[i] + 1)
print(dp[target])