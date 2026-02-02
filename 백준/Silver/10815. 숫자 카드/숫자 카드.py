n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
query = list(map(int, input().split()))

for a in query:
    l,r = 0, n
    exist = False
    while l<r:
        mid = (l+r)//2
        if arr[mid]< a:
            l = mid+1
        elif arr[mid] > a:
            r = mid
        else:
            r=  mid
            exist= True
    print(1 if exist else 0, end = " ")
