# Q1
# arr = [5, 7, 1, 2, 9, 3]
# target = 4
#
# arr.sort()
# i = 0
# j = len(arr)-1
#
# while i < j:
#     if arr[i] + arr[j] == target:
#         print(arr[i], arr[j])
#         break
#     elif arr[i] + arr[j] > target:
#         j -= 1
#     else:
#         i += 1


# Q2
# maximum sum subarray
li = [-2,1,-3,4,-1,2,1,-5,4]


def maxSubArray(a):
    max_ele = a[0]
    max_end = 0

    for i in range(0, len(a)):
        max_end = max_end + a[i]
        if max_end < 0:
            max_end = 0

        elif max_ele < max_end:
            max_ele = max_end
    return max_ele


print(maxSubArray(li))