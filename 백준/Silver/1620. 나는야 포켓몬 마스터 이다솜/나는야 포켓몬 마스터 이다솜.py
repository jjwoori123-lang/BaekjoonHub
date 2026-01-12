n, m = map(int, input().split())
dex = dict()
dex1 = dict()
for i in range(n):
    x = input()
    if x not in dex:
        dex[x] = str(i+1)
        dex1[str(i+1)] = x
for j in range(m):
    x = input()
    if x in dex1:
        print(dex1[x])
    else:
        print(dex[x])
