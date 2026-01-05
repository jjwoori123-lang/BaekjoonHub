import heapq
n = int(input())
a = int(input())
list_a = []
heapq.heapify(list_a)
heapq.heappush(list_a, a)
for i in range(n-1):
    heapq.heappush(list_a, int(input()))
for _ in range(n):
    print(heapq.heappop(list_a))    
