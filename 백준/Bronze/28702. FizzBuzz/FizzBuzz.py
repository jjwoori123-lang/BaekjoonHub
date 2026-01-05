max_n = 3
lista = []
for _ in range(max_n):
    lista.append(input())
flag = 0
for i in range(max_n-1, -1, -1):
    if lista[i].isnumeric():
        flag = i
        break
res = (int(lista[flag]) + max_n - flag)
if res % 3 == 0:
    print("Fizz", end = "")
if res % 5 == 0:
    print("Buzz", end = "")
if res % 5 and res % 3:
    print(res)