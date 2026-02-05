import heapq
n,m  = map(int, input().split())
graph = [[] for _ in range(n+1)]

dist = [int(1e9)] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0, start))
    dist[start] = 0
    while pq:
        dis, node = heapq.heappop(pq)
        if dist[node] < dis: continue
        for nnode, ndist in graph[node]:
            cost = dis + ndist
            if dist[nnode] > cost:
                dist[nnode]  = cost
                heapq.heappush(pq, (cost, nnode))
dijkstra(1)
print(dist[-1])