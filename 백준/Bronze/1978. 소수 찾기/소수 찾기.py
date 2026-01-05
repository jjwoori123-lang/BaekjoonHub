import math
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    if a == 1:
        cnt+=1
        continue
    else:
        for i in range(2, int(math.sqrt(a)) +1):
            if a % i == 0:
                cnt +=1
                break
print(n-cnt)