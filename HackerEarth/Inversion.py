# For a 2D matrix(M) find number of inversion
# {(x1,y1),(x2,y2)} x1<=x2 and y1<=y2 such that M(x1,y1) > M(x2,y2)

"""
First line consists of a single integer T denoting the number of test cases.
First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers
denoting the matrix M.
"""
from numpy import matrix

T = int(input())
while T != 0:
    N = int(input())
    M = []
    for i in range(N):  # A for loop for row entries
        for j in range(N):  # A for loop for column entries
            M.append(int(input()))

        matrix.append(M)


    def update(l, r, val, bit):
        i = l
        while i <= N:
            j = r
            while j <= N:
                bit[i][j] += val
                j += j & -j
            i += i & -i


    # function to find cumulative sum upto
    # index (l, r) in the 2D BIT


    def query(l, r, bit):
        ret = 0
        i = l
        while i > 0:
            j = r
            while j > 0:
                ret += bit[i][j]
                j -= j & -j
            i -= i & -i

        return ret


    # function to count and return the number
    # of inversion pairs in the matrix


    def countInversionPairs(mat):
        # the 2D bit array and initialize it with 0.
        bit = [[0 for i in range(N + 1)] for j in range(N + 1)]

        # v will store the tuple (-mat[i][j], i, j)
        v = []

        # store the tuples in the vector v
        for i in range(N):
            for j in range(N):
                # Note that we are not using the pair
                # (0, 0) because BIT update and query
                # operations are not done on index 0
                v.append([-mat[i][j], [i + 1, j + 1]])

        # sort the vector v according to the
        # first element of the tuple, i.e., -mat[i][j]
        v.sort()

        # inv_pair_cnt will store the number of
        # inversion pairs
        inv_pair_cnt = 0

        # traverse all the tuples of vector v
        i = 0
        while i < len(v):

            curr = i

            # 'pairs' will store the position of each element,
            # i.e., the pair (i, j) of each tuple of the vector v
            pairs = []

            # consider the current tuple in v and all its
            # adjacent tuples whose first value, i.e., the
            # value of –mat[i][j] is same
            while curr < len(v) and (v[curr][0] == v[i][0]):
                # push the position of the current element in 'pairs'
                pairs.append([v[curr][1][0], v[curr][1][1]])

                # add the number of elements which are
                # less than the current element and lie on the right
                # side in the vector v
                inv_pair_cnt += query(v[curr][1][0], v[curr][1][1], bit)
                curr += 1

            # traverse the 'pairs' vector
            for it in pairs:
                x = it[0]
                y = it[1]

                # update the position (x, y) by 1
                update(x, y, 1, bit)

            i = curr

        return inv_pair_cnt


    print(countInversionPairs(M))

    T -= 1
