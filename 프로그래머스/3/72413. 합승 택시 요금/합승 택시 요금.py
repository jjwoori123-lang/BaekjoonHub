def solution(n, s, a, b, fares):
    graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    for u,v,w in fares:
        graph[u][v] = w
        graph[v][u] = w
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    ans = graph[s][a] + graph[s][b] 
    for k in range(1, n+1):
        ans = min(ans, graph[s][k] + graph[k][a] + graph[k][b])
    return ans