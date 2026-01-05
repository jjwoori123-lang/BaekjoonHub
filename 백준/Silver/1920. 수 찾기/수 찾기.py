n = int(input())
list1 = list(map(int, input().split()))
dict1 = dict()
for i in range(len(list1)):
    dict1[list1[i]] = dict1.get(list1[i], 1)
m = int(input())
dict2 = list(map(int, input().split()))
flg = False

res = [0] * m
for i in range(len(dict2)):
    if dict2[i] in dict1:
        res[i] = 1
for i in range(m):
    print(res[i])
