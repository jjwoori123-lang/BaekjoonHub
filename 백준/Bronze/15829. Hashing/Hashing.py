import sys
input = sys.stdin.readline
n = int(input())
mod = 1234567891
s = input().strip()
res = 0
multi = [1]
for i in range(50):
    multi.append(multi[-1] * 31 % mod)
for i in range(n):
    res += (int(ord(s[i]) - ord("a")) + 1) % mod  *  multi[i] % mod
print(res % mod)