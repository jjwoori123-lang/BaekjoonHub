import sys
sys.setrecursionlimit(100000)

def find(x):
    if x!= parent[x]:parent[x] =  find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:parent[b] = a
    else:parent[a] = b

n,m  = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b,c, = map(int, input().split())
    if a == 0: union(b,c)
    else:
        if find(b) == find(c):print("YES")
        else:print("NO")