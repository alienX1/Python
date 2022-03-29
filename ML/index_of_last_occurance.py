# You are given sorted array. An element is given, check weather it is present or not. If present return index of its 
# last occurrence

li = [2, 2, 2, 3, 4, 6, 6, 6, 9, 10]

n = int(input())
if n in li:
    print('Yes')

    index_list = []
    for i in range(0, len(li)):
        if n == li[i]:
            index_list.append(i)
    print(max(index_list))
else:
    print('Not present')
