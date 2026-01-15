def dfs(idx, add, sub, mul, div, val):
    global max_res, min_res
    if add + sub + mul+ div == 0:
        max_res = max(max_res, val)
        min_res = min(min_res, val)
        return 
    else:
        if add:
            dfs(idx+1, add-1, sub, mul, div, val+arr[idx+1])
        if sub:
            dfs(idx+1, add, sub-1, mul, div, val-arr[idx+1])
        if mul:
            dfs(idx+1, add, sub, mul-1, div, val*arr[idx+1])
        if div:
            dfs(idx+1, add, sub, mul, div-1, int(val/arr[idx+1]))
n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split())) #덧셈, 뺄셈, 곱셈, 나눗셈
max_res, min_res = -int(1e9), int(1e9)
dfs(0, op[0], op[1], op[2], op[3], arr[0])
print(max_res)
print(min_res)