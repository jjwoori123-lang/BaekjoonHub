n = int(input())
list1 = list(map(int, input().split()))
dic1 = {}
for l in list1:
    if l not in dic1:
        dic1[l] =1
    else:
        dic1[l] +=1
m = int(input())
list2 = list(map(int, input().split()))

for l in list2:
    if l in dic1:
        print(dic1[l], end = " ")
    else:
        print(0, end = " ")