import heapq
n = int(input())
com = [int(input()) for _ in range(n)]
q = []
for i in range(n):
    if com[i] == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -com[i])