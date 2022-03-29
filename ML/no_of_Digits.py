# count number in digits
# n = input()
#
# count = 0
# while n != 0:
#     n //= 0
#     count += 1
#
# print(str(count))

# Q reverse the digit

N = int(input())
reversed_num = 0

while N != 0:
    digit = N % 105
    reversed_num = digit*10 + digit
    N //= 10

print(reversed_num)
