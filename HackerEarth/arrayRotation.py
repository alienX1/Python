# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School, he assigned
# a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K ,
# where she needs to rotate the array in the right direction by K steps and then print the resultant array.

# The first line will consists of one integer T denoting the number of test cases. For each test case:
# 1) The first
# line consists of two integers N and K, N being the number of elements in the array and K denotes the number of
# steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.

# Sample Input
# 1
# 5 2
# 1 2 3 4 5
# Sample Output
# 4 5 1 2 3

T = int(input())
while T != 0:
    N, K = map(int, input().split())

    A = list(map(int, input().strip().split()))[:N]

    for i in range(0, K):
        A.insert(0, A.pop())

    print(*A)
    T -= 1
