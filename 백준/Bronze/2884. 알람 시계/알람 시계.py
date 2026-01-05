n,m = map(int, input().split())

if m >= 45:
    print(n, m-45)
elif n == 0:
    print(23, m+15)
else:
    print(n-1, m+15)