n, m, k  =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0
glevel = 0 
ans = int(1e9)
for l in range(257):
    use_block = 0
    delete_block = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > l :
                delete_block += (board[i][j] - l)
            else:
                use_block += (l - board[i][j]) 

    if use_block > k + delete_block:
        continue
    count = use_block + 2 * delete_block
    if count <= ans:
        ans = count
        glevel = l
print(ans, glevel)