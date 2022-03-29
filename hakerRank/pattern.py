# row = int(input())

# for i in range(1, row+1):
#     for j in range(1, i):
#         print(j,end=" ")
#     print()

# for i in range (1, row+1):
#     j = row
#     while j>i:
#         print(" ",end=" ")
#         j -= 1
#     for k in range(1, i+1):
#         print(k,end=" ")
#     print()

a = 10
b = 12
c = 15


# maxValue = max(a,b,c)
# print(maxValue)

maxValue = max(a,b,c)

if maxValue == a:
    print("a is max")
elif maxValue == b:
    print("b is max")
else:
    print("c is max")