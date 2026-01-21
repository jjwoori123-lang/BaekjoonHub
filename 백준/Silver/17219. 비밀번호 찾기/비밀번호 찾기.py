n, m = map(int, input().split())
dic1 = dict()

for _ in range(n):
    k,v = input().split()
    if k not in dic1: dic1[k] = v

for _ in range(m):print(dic1[input()])