from collections import deque
import sys

input =sys.stdin.readline
n, m =  map(int, input().split())
arr = []
arr.append(deque(list(map(int, input().split()))))
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def stacked(graph):
    q = graph[0].popleft()
    graph.append(deque([q]))
def rot_90(graph):
    new = [[0] * len(graph) for _ in range(len(graph[0]))]
    for i in range(len(graph[0])):
        for j in range(len(graph)):
            new[i][j] = graph[j][len(graph[0]) - i-1]
    return new
def fly_block(graph):
    while True:
        if len(graph) > len(graph[0]) - len(graph[-1]): #이거 90도
            break

        fly_blk = []
        fly_blk_row = len(graph)
        fly_blk_col = len(graph[-1])

        for i in range(fly_blk_row):
            new = deque()
            for _ in range(fly_blk_col):
                new.append(graph[i].popleft())
            fly_blk.append(new)
        graph = [graph[0]]
        rot_block = rot_90(fly_blk)
        for r in rot_block:
            graph.append(deque(r))
    return graph
def fix_fishnum(graph):
    dp = [[0] * len(graph[x]) for x in range(len(graph))]
    for x in range(len(graph)):
        for y in range(len(graph[x])):
            for d in direction:
                nx, ny = x+d[0], y+d[1]
                if 0<=nx<len(graph) and 0<=ny< len(graph[nx]):
                    if graph[x][y] > graph[nx][ny]:
                        d = (graph[x][y] - graph[nx][ny])//5
                        if d>=1:
                            dp[x][y] -=d
                    else:
                        d = (-graph[x][y] + graph[nx][ny])//5
                        if d>=1:
                            dp[x][y] +=d
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] += dp[i][j]


def flatten(graph):
    new_graph = deque()
    for i in range(len(graph[-1])):
        for j in range(len(graph)):
            new_graph.append(graph[j][i])
    for i in range(len(arr[-1]), len(graph[0])):
        new_graph.append(graph[0][i])
    result = []
    result.append(new_graph)
    return result

def rot180(graph):
    new_graph = []
    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])
    return new_graph

def fly_block2(graph):
    left1 = list()
    left2 = list()
    new_deque1 = deque()
    for i in range(n//2):new_deque1.append(graph[0].popleft())
    left1.append(new_deque1)
    rot_left = rot180(left1)
    graph+=rot_left

    for i in range(2):
        temp_deque = deque()
        for _ in range(n//4):
            temp_deque.append(graph[i].popleft())
        left2.append(temp_deque)
    rot_left2 = rot180(left2)
    graph += rot_left2

def get_result(graph):
    dq = graph[0]
    result1 = max(dq) - min(dq)    
    return result1

answer = 0
while True:
    result = get_result(arr)
    if result <= m:
        print(answer)
        break
    min_val = min(arr[0])
    arr[0] = deque([f+1 if f == min_val else f for f in arr[0]])
    stacked(arr)
    arr = fly_block(arr)
    fix_fishnum(arr)
    arr = flatten(arr)
    fly_block2(arr)
    fix_fishnum(arr)
    arr = flatten(arr)
    answer += 1