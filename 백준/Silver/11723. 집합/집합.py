import sys
input = sys.stdin.readline
n = int(input())
start = 0
for _ in range(n):
    cal = list(input().split())
    if len(cal) == 1:
        if cal[0] == 'all':
            start =  (1 << 20) - 1
            start = int(start)
        else:
            start = 0
    else:
        a,b = cal
        b = int(b)
        if cal[0] == 'add':
            start |= 1<<(b-1)
        elif cal[0] == 'remove':
            start &= ~( 1 << (b-1))
        elif cal[0] == 'check':
            chk  = start & ( 1 << (b-1))
            if chk: 
                print(1)
            else:
                print(0)
        elif cal[0] == 'toggle':
            start ^= ( 1 << (b-1))
