def solution(s):
    answer = True
    res = []
    for i in range(len(s)):
        if not res and s[i] == '(':
            res.append(s[i])
        elif res and res[-1] == '(':
            if s[i] == '(':
                res.append(s[i])
            else:
                res.pop()
        else:
            return False
    if res:
        return False
    return True