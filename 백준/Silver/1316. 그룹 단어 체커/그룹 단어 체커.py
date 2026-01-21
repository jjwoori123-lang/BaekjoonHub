n = int(input())
res = 0
for _ in range(n):
    chk = True
    stack = []
    s = list(input())
    stack.append(s[0])
    for j in range(1, len(s)):
        if stack[-1] == s[j]:
            pass
        else:
            if s[j] in stack:
                chk = False
            else:
                stack.append(s[j])
    if chk:
        res+=1
print(res)