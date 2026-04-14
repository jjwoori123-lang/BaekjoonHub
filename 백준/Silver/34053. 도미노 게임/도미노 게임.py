n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
total_sum = 0
has_zero = False
min_value = float('inf')
for i in range(n):
    for j in range(m):
        val  = arr[i][j]
        total_sum += val
        if val == 0:
            has_zero = True
        if val < min_value:
            min_value = val

if has_zero:
    print(total_sum )
else:
    print(total_sum - min_value)