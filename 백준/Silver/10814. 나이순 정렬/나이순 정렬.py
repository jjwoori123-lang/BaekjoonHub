n = int(input())
arr = [list((input().split())) for _ in range(n)]
arr = sorted(arr, key = lambda x : int(x[0]))
for i in range(n):
    print(*arr[i])