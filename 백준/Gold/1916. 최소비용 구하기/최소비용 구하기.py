import heapq

def dijkstr(s,e):
    q = []
    heapq.heappush(q, (0, s))
    while q:
        cost, start = heapq.heappop(q)
        if cost > visit[start]: continue
        for nxt, ncost in graph[start]:
            ndist = ncost + cost
            if visit[nxt] < ndist: continue
            if visit[nxt] > ndist:
                visit[nxt] = ndist
                heapq.heappush(q, (ndist, nxt))

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
s,e = map(int, input().split())
visit = [int(1e9)] * (n+1)
visit[s] = 0
dijkstr(s,e)
print(visit[e])