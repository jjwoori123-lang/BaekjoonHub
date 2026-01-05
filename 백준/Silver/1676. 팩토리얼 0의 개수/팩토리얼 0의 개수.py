n = int(input())
tmp = 1
cnt = 0
for i in range(n, 1, -1):
    tmp *=i
    if tmp % 10 == 0:
        tmp //= 10
        cnt+=1
print(cnt)