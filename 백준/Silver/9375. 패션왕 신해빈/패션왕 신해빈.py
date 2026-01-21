t = int(input())
for _ in range(t):
    n  = int(input())
    dic = dict()
    cnt = 1
    for i in range(n):
        a,b = input().split()
        if b not in dic: dic[b] = 1
        else: dic[b]+=1
    for k,v in dic.items():
        cnt *= (v+1)
    print(cnt-1)
    