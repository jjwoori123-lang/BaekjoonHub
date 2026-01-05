n = int(input())
cnt = 1
n-=1
if n > 0:
    for i in range(1, int(n//6) + 1):
        if n - (i * 6) >= 0:
            cnt+=1
            n -= i * 6
        else:
            break
if n:
    cnt+=1
print(cnt)