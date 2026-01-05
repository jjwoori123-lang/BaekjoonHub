n=  int(input())
arr = list(map(int, input().split()))
sum_arr = sum(arr)
ind = max(arr)
res = sum_arr  * 100 / ind / n
print(res) 