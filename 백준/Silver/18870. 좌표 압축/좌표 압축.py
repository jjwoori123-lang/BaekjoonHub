n = int(input())
arr = list(map(int, input().split()))

sorted_list = sorted(list(set(arr)))
res = dict(zip(sorted_list, range(len(sorted_list))))
for a in arr:
    print(res[a], end = " ")
