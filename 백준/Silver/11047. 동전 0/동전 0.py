num, target = map(int, input().split())
coins = []
for _ in range(num):
    coins.append(int(input()))
coins.sort(reverse = True)
ans  = 0

for c in coins:
    if c <= target:
        a,b = int(target // c), target % c
        ans+=a
        target = b
print(ans) 