t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    arr.sort()
    for i in range(len(arr2)):
        l, r = 0, len(arr) - 1
        flag = False
        while l<=r:
            m = (l+r)//2
            if arr[m] == arr2[i]:
                print(1)
                flag = True
                break
            if arr[m] > arr2[i]:
                r = m-1
            elif arr[m] < arr2[i]:
                l = m+1
        if not flag: print(0)
        else: pass