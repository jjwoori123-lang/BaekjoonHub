s = [[1,0], [0,1], [1,1]]

n = int(input())
for i in range(3, 41):
    s1 = s[i-1][0] + s[i-2][0]
    s2 = s[i-1][1] + s[i-2][1]
    s.append([s1, s2])

for _ in range(n):
    a = int(input())
    print(*s[a])