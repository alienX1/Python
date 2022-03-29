# Using the function Map, count the number of words that start with ‘S’ in input_list.

# input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi']
#
#
# print(sum(map(lambda x: x[0] == 'S', input_list)))

# input_list = [['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]
#
# print(list(map(' '.join, zip(*input_list))))

# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#
# print(list(filter(lambda x: (x % 5 == 0), input_list)))

# input_list = ['soap','sharp','shy','silent','ship','summer','sheep']
#
# print(list(filter(lambda x: (x[0] == 's') and (x[-1] == 'p'), input_list)))

# input_list = ['All','you','have','to','fear','is','fear','itself']
# print(' '.join(input_list))

from functools import reduce
input_list = [65,76,87,23,12,90,99]
print(reduce(max, input_list))
