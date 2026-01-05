def solution(info, n, m):
    answer = 0
    dp  = {0:0}
    for x,y in info:
        rob = {}
        for k,v in dp.items():
            if k + x < n: rob[k+x] = min(rob.get(k+x, v), v)
            if v + y < m: rob[k] = min(rob.get(k, v+y), v+y)
        dp = rob
    return min(dp) if len(dp) else -1