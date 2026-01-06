import sys
input = sys.stdin.readline
n, m = input().split()
visit = [int(n)]
while True:
    c = 0
    for a in n:
        c+= int(a) ** int(m)
    if c not in visit:
        visit.append(c)
        n = str(c)
    else:
        print(visit.index(c))
        break
