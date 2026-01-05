n, m = map(int, input().split())
res = 1
for i in range(n-m+1, n+1):
    res *= i
for j in range(1, m+1):
    res /= j
print(int(res))
