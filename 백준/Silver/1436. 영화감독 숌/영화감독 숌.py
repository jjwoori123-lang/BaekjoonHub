import sys
input = sys.stdin.readline
n = int(input())
dict = {}
cnt = 0
target = 666
while target:
    if "666" in str(target):
        cnt+=1
        dict[cnt]  = target
        if cnt == n:
            print(dict[n])
            break
    target+=1
