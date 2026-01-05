import sys
input = sys.stdin.readline
n = int(input())
lista = [0 for i in range(10001)]
for _ in range(n):
    lista[int(input())] += 1
for i in range(10001):
    while lista[i] > 0:
        print(i)
        lista[i]-=1