import sys
input = sys.stdin.readline
set1 = set(list())
for _ in range(int(input())):
    list_a = list(input().split())
    if len(list_a) == 2:
        a,b = list_a
        if a == "add":
            set1.add(int(b))
        if a == 'check':
            if int(b) in set1:
                print(1)
            else:
                print(0)
        if a == 'remove':
            if int(b) in set1:
                set1.discard(int(b))
        if a == 'toggle':
            if int(b) in set1:
                set1.discard(int(b))
            else:
                set1.add(int(b))
    elif len(list_a) == 1:
        if list_a[0] == "all":
            set1 = set([i for i in range(1,21)])
        else:
            set1 = set(list())
        