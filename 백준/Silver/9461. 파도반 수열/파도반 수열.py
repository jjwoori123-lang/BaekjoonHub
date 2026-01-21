t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] * (101)
    arr[1], arr[2], arr[3] = 1,1,1
    for i in range(4, n+1):
        arr[i] = arr[i-2] + arr[i-3]
    print(arr[n])