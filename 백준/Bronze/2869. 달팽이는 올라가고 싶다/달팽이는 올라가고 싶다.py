import sys
import math
input = sys.stdin.readline
a,b,v = map(int, input().split())
start = 0
cnt = 1
v -=a
if v <= 0:
    print(cnt)
else:
    print(cnt + math.ceil(v / (a-b)))
