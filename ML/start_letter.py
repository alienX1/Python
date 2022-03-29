# Write a code to check if the string in input_str starts with a vowel or not. Print capital YES or NO.

import sys
input_str = sys.stdin.read()

# Write your code here
first_chr = input_str[0]
vowel = ['a', 'e', 'i', 'o', 'u']
# Use capital YES or NO
if first_chr in vowel:
    print('YES')
else:
    print('NO')

# L1 = [10, 20, 30, 24, 18]
# L2 = [8, 14, 15, 20, 10]
# L3 = []
# for i in range(len(L1)):
#     L3.append(L2[i] - L1[i])
# print(L3)
