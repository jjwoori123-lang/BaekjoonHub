n = input()
res = 0
flag = 0
for i in range(len(n)):
    if n[i] == "*":
        flag = i
        pass
    elif i % 2:
        res += int(n[i]) * 3
    else:
        res += int(n[i])

if flag % 2:
    for i in range(10):
        if (res + i *3) % 10 == 0:
            print(i)
            break 
else:
    for i in range(10):
        if (res + i) % 10 == 0:
            print(i)
            break 