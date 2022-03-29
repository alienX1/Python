import math


# Addition Function
def add(x, y):
    return x + y


# Subtraction function
def subtract(x, y):
    return x - y


# Multiplication function
def multiply(x, y):
    return x * y


# Division function
def divide(x, y):
    return x / y


# LCM function
def lcm(x, y):
    return math.lcm(x, y)


# HCf function
def hcf(x, y):
    HCF = 1
    for i in range(2, x + 1):
        if x % i == 0 and y % i == 0:
            HCF = i
    return HCF


# Log function
def Log(x, y):
    return math.log(x, y)


print('Select operation')
print('1.for addition,'
      ' 2.for subtraction, '
      ' 3.for multiplication, '
      ' 4.for division, '
      ' 5.for LCM, '
      ' 6.for HCF, '
      ' 7.for log ')


def calculation():
    while True:
        # Takes operation user want to perform
        operation = input('Enter choice from 1/2/3/4/5/6/7 : ')
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter Second Number: '))
        if operation == '1':
            print(add(num1, num2))
        elif operation == '2':
            print(subtract(num1, num2))
        elif operation == '3':
            print(multiply(num1, num2))
        elif operation == '4':
            print(divide(num1, num2))
        elif operation == '5':
            print(lcm(num1, num2))
        elif operation == '6':
            print(hcf(num1, num2))
        elif operation == '7':
            print(Log(num1, num2))
        else:
            print('Enter valid operation')


calculation()
