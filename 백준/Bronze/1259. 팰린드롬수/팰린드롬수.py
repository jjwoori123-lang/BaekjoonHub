import sys
input = sys.stdin.readline
while True:
    n = input().strip()
    if n == "0":
        break
    flag = True
    for i in range(0, int(len(n)//2)+1):
        if n[i] != n[len(n)-1 -i]:
            flag = False
            print("no")
            break
    if flag:
        print("yes")