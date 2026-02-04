n = int(input())
m = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
    

parent = [i for i in range(n)]
for i in range(n):
    cord = list(map(int, input().split()))
    for c in range(len(cord)):
        if cord[c] == 1:
            union(i,c)

lista= list(map(int, input().split()))
init = lista[0]
chk = True
for i in range(1, m):
    if find(init-1) != find(lista[i]-1):
        chk = False
if chk: print("YES")
else: print("NO")