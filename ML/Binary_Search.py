# def binary():
#     list1 = [2, 4, 5, 6, 7, 8, 10, 12, 15, 20]
#     n = int(input('Enter number you wanna search: '))
#     low = 0
#     high = len(list1) - 1
#
#     while low <= high:
#         mid = (low + high)//2
#         if list1[mid] == n:
#             print(n)
#             return mid
#         elif list1[mid] < n:
#             low = mid + 1
#         else:
#             high = mid - 1
#     print('Element not found')
#     return -1
#
#
# binary(n)

li = [1, 0, 4, 0, 0, 0, 9, 0, 5, 3, 0, 1]
# after operation
# li = [1,4,9,5,3,0,0,0,0,0]


for i in li:

    if i == 0:
        li.remove(i)
        li.append(i)

print(li)


def sub(str1, sub1):
    t = 0
    l = len(str1)
    for i in range(l):
        if (t == len(sub1)):
            break
        if str1[i] == sub1[t]:
            t += 1
        else:
            t = 0
            if str1[i] == sub1[t]:
                t += 1
    if (t < len(sub1)):
        return -1
    else:
        return i - t
    # O(1) and O(N)


sub("abaacda", 'acd')

str1 = "shubham"
str2 = "husambh"

dict1, dict2 = {}, {}
for i in str1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 0

for i in str2:
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 0

flag = True
for i in dict1:
    if dict1[i] != dict2[i]:
        flag = False
        break
if flag:
    print('anagram')
