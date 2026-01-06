def dfs(p): #일단 p부터 시작한다고 가정한다
    child = arr[p]
    if not visit[child]:
        visit[child] = 1
        dfs(child)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (n+1)
    #조회하는 순열을 찾기 위해서는 재귀 함수를 짜는게 맞기는 함
    cnt = 0
    for i in range(1, n+1):
        if not visit[i]:
            visit[i] = 1
            dfs(i)
            cnt+=1
    print(cnt)
