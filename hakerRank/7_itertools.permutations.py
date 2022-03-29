from itertools import permutations

# print(permutations(['1', '2', '3']))

# print(list(permutations(['1', '2', '3'])))
# print(list(permutations(['1', '2', '3'], 2)))
# print(list(permutations('abc',2)),'n')

s = "HACK"
k = 2
# s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')
