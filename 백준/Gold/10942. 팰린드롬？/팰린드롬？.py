import sys
input = sys.stdin.readline
t = int(input())
arr = [0] + list(map(int, input().split()))
n = int(input())

dp = [[0] * (t+1) for _ in range(t+1)]

for i in range(1, t+1):
    dp[i][i] = 1 # 이거는 무조건 맞음

for i in range(1, t):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for i in range(t-2, 0, -1):
    for j in range(i+2, t+1):
        if arr[i] == arr[j] and dp[i+1][j-1]:
            dp[i][j] = 1
for _ in range(n):
    a,b = map(int, input().split())
    print(dp[a][b])