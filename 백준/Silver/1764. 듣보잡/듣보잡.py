n,m = map(int, input().split())

v1 = set()
v2 = set()

for i in range(n):
    v1.add(input())

for i in range(m):
    v2.add(input())

r = list(v1.intersection(v2))
r.sort()
print(len(r))
for i in range(len(r)):
    print(r[i])