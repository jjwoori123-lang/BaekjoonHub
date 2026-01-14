import heapq

n = int(input())
list_a = []
for _ in range(n):
    list_a.append(int(input()))
if n == 1:
    print(0)
else:
    heapq.heapify(list_a)
    total = 0
    while len(list_a)>1:
        f = heapq.heappop(list_a)
        s = heapq.heappop(list_a)
        sum_v  = f+s
        total += sum_v
        heapq.heappush(list_a, sum_v)
    print(total)
