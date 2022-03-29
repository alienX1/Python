# You have given an array if maximum number of item greater than (size of array)/2 return number
l1 = [1, 2, 1, 2, 1]

# m1
# freqMap = dict()
# for n in l1:
#     if num in freqMap:
#         freqMap[n] += 1
#
#     else:
#         freqMap[n] = 1
#     if freqMap[n] > len(l1)/2:
#         return n

# m2


# MAX PRODUCT OF 3
import sys


def maxProduct(arr):
    n = len(arr)
    # If size is less than 3, no
    # triplet exists
    if n < 3:
        return -1

    # Initialize Maximum, second
    # maximum and third maximum
    # element
    maxA = -sys.maxsize - 1
    maxB = -sys.maxsize - 1
    maxC = -sys.maxsize - 1

    # Initialize Minimum and
    # second minimum element
    minA = sys.maxsize
    minB = sys.maxsize

    for i in range(n):

        # Update Maximum, second
        # maximum and third maximum
        # element
        if arr[i] > maxA:
            maxC = maxB
            maxB = maxA
            maxA = arr[i]

        # Update second maximum and
        # third maximum element
        elif arr[i] > maxB:
            maxC = maxB
            maxB = arr[i]

        # Update third maximum element
        elif arr[i] > maxC:
            maxC = arr[i]

        # Update Minimum and second
        # minimum element
        if arr[i] < minA:
            minB = minA
            minA = arr[i]

        # Update second minimum element
        elif arr[i] < minB:
            minB = arr[i]

    return max(minA * minB * maxA,
               maxA * maxB * maxC)


# arr = [10, 3, 5, 6, 20]
arr_li = [-2, 4, 8, -12, 11, 14]

max_triplet = maxProduct(arr_li)
if max == -1:
    print("No such Triplet")
else:
    print(max_triplet)
