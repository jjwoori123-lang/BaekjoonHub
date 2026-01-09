def solution(n):
    cnt= str(bin(n)).count("1")
    for i in range(n+1, 1000065):
        if str(bin(i)).count("1") == cnt:
            return i