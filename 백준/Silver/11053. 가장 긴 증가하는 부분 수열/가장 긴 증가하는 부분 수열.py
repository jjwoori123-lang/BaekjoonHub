n = int(input())

list_a  = list(map(int, input().split()))

dp = [1] * n

for i in range(n-1):
    for j in range(i+1, n):
        if list_a[i] < list_a[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
