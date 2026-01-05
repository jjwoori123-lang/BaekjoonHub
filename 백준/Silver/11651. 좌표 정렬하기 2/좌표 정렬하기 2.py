n = int(input())
arr_list = [list(map(int, input().split())) for _ in range(n)]
arr_list = sorted(arr_list, key = lambda x: (x[1], x[0]))

for a in arr_list:
    print(*a)