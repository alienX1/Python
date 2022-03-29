from itertools import combinations

# print(list(combinations('12345', 2)))
# A = [1,1,3,3,3]
# print(list(combinations(A, 4)))

a = input().split()

for i in range(1, int(a[1]) + 1):
    for j in combinations(sorted(a[0]), i):
        print(''.join(j))
