s = list(input().split("-"))
l = len(s)
if l == 1:
    print(sum(list(map(int, s[0].split("+")))))
else:
    res = sum(list(map(int, s[0].split("+"))))
    for a in s[1:]:
        tmp = 0
        x = list(map(int, a.split("+")))
        tmp = sum(x)
        res -= tmp
    print(res)