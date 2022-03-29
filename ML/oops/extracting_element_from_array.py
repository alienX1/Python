# import numpy as np
# import ast
#
#
# input_list = ast.literal_eval(input())
# m = int(input())
# n = int(input())
# array_1 = np.array(input_list)
# final_array = array_1[(array_1 > m) & (array_1 < n)]
# print(final_array)

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# def f(value, values):
#     v = 1
#     values[0] = 44
#
#
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# arr = [1, 2, 3, 4, 5, 6]
# print(arr[-1])
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end=" ")

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
#
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#     return v
#
#
# print(fun(data[0]))

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())