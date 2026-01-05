n = int(input())
word_a = list()
for _ in range(n):
    word_a.append(input())
word_a = list(set(word_a))
word_a = sorted(word_a, key= lambda x: (len(x), x))
for i in range(len(word_a)):
    print(word_a[i])