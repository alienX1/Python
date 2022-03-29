# you are given a list you to reverse it
# def Reverse(list):
#     return [ele for ele in reversed(list)]

# list = [100, 10, 5, 400, 1]
# print(Reverse(list))

# Q1
# list1 = ['H', 'a', 'y']
# list2 = ['ow', 're', 'ou']
#
# for i, j in zip(list1, list2):
#     print(i+j,end=" ")

# Q2
# list1 = [5, 4, 12, 2]
# for i in list1:
#     print(i*i, end=" ")

# Q3
# l1 = ['Say', 'Hi']
# l2 = ['Hello', 'My', 'Brother']
#
# l2.reverse()
# for i in l1:
#     for j in l2:
#         print(i+" "+j)

# m2

# for i in range(len(l1)):
#     for j in range(len(l2)-1,-1,-1):
#         print(l1[i]+" "+l2[j])

# Q4
# import ast,sys
# input_str = (sys.stdin.read()).split(',')
# input_str.insert(1, '&')
# string_1 = ' '.join(map(str, input_str))  # Type your answer here
# print(string_1)

# Q5
# Print common element in sorted order
# import ast, sys
# input_str = sys.stdin.read()
# input_list = ast.literal_eval(input_str)
# list_1 = input_list[0]
# list_2 = input_list[1]

# Type your answer here
# answer = list(set(list_1).intersection(set(list_2)))
#
# print(answer)


# Q
# nums = set([1,1,2,3,3,3,4])
# print(len(nums))

# d = {'Python':40, 'R':45}
# print(list(d.keys()))

# d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
# p = list(d.values())
# p.sort()
# print(p)
# print(len(p))

# Q Employee_data = {101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22,
# 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29,
# 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27,
# 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38,
# 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27,
# 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44,
# 176: 27, 177: 30, 178: 26, 179: 27}
#
# Employee_data.update({104:27, 140:27, 164:27}) Employee_data.pop(143)
#
# print(sum(Employee_data.values())/len(Employee_data))

