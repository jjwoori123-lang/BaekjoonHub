import math
n = int(input())
arr = [1e9] * (1+n)
arr[0] = 0
for i in range(1, n+1):
    j = 1
    while i  >= j*j:
        if arr[i]  > arr[i-j*j] + 1:
            arr[i] = min(arr[i], arr[i-j*j] + 1)
        j+=1
print(arr[-1])