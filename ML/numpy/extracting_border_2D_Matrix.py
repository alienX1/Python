# # Extract all the border rows and columns from a 2-D array.
# import ast,sys
# input_str = sys.stdin.read()
# input_list = ast.literal_eval(input_str)
#
# import numpy as np
#
# # Convert the input list to a NumPy array
# array_2d =np.array(input_list)
#
# # Extract the first column, first row, last column and last row respectively using
# # appropriate indexing
# col_first = column[0] for column in array_2d
# row_first = array_2d[len(array_2d):2]
# # col_last = array_2d[0:len(array_2d)]
# # row_last = array_2d[0:len(array_2d)]
# print(col_first)


# import numpy as np
# np1 = np.arange(5,51,5)
# print(np1)

class A:
    def __init__(self, num):
        num = 3
        self.num = num

    def change(self):
        self.num = 7


a = A(5)
print(a.num)
a.change()
print(a.num)
