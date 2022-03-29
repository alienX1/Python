"""
You are given a two lists A and B. Your task is to compute their cartesian product AXB.
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""
from itertools import product
A = input().split()
A = list(map(int,A))
print(A)

B = input().split()
B = list(map(int, B))
print(B)

output = list(product(A,B))
for i in output:
    print(i, end=" ")
