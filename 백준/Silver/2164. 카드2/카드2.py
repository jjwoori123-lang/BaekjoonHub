# 덱을 쓰면 쉽게 풀수도?

from collections import deque
n  = int(input())
q = deque([i+1 for i in range(n)])
cnt = 0
while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    x = q.popleft()
    q.append(x)
print(q.popleft())