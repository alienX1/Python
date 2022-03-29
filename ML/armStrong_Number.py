# Function to print armstrong number
# ArmStrong Number = Number that is sum of cubes of each digit
def armStrong(n):
    sum = 0
    temp = n
    while n > 0:
        digit = n % 10
        sum += digit ** 3
        n //= 10
    if temp == sum:
        print(temp, "is an armstrong number")
    else:
        print(temp, "is not an armstrong number")
        
        
num = int(input("Enter a number: "))
armStrong(num)