# var1 = 6
# var2 = 56
# var3 = int(input())
# if var3>var2:
#     print("Greater")
# elif var3==var2:
#     print("Equal")
# else:
#     print("Lesser")

# list1 = [5, 7, 3]
# print(15 not in list1)
# if 15 not in list1:
#     print("No its not in the list")

# Quiz
# print("What is your age?")
# age = int(input())
# if age<18:
#     print("You cannot drive")
#
# elif age==18:
#     print("We will think about you")
#
# else:
#     print("You can drive")


# num = 0
# sum = 0
# while True:
#     number = input("Enter a number ")
#     if number == '1':
#         break
#     try :
#         num1 = float(number)
#     except:
#         print('Invailed Input')
#         continue
#     num = num+1
#     sum = sum + num1
# print (sum)

n = int(input("enter number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("Perfect number!")
else:
    print("Not a Perfect number!")