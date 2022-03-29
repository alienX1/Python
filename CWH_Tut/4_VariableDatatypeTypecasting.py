"""
a = 34 # Variable storing an integer
b = 23.2 # Variable storing real number

# Variable in Python:
abc = "It's a string variable"
_abcnum = 40 # It is an example of int variable
abc123 = 55.854 # It is an example of float variable
print(_abcnum + abc123) # This will give sum of 40 + 55.854

# type() Function in Python:
harry = "40"
demo = 55.5
demo2 = 40
print (type(harry)) #It will give output as string type
demo3 = type(demo) #It will return data type as float
print(demo3) #It will print that data type
print(type(demo2)) #It will give output as int type
"""
# var1 = "It's a String"
# var2 = 5
# print(var1+var2)
''' It will give an error as we can't add string to any number. '''

# Concatenate
# var1 = "My Name is "
# var2 = "Harry"
# var3 = var1+var2+" & I am a Good Boy."
# print(var1+var2) # It will give output 'My Name is Harry'
# print(var3)

# Typecasting in Python :
"""
Typecasting is the way to change one data type of any data or variable to 
another datatype, i.e. it changes the data type of any variable to some 
other data type.
"""
abc = 5
abc2 = '45'
abc3 = 55.95
xyz = 5.0

abc4 = int(abc2)

print(abc + abc4)  # Output : 50
print(abc + int(abc2))  # Output : 50

print(float(abc) + xyz)  # It will add 5.0 + 5.0 and will return 10.0

# print(str(abc) + 45)  # It will give an error as abc has been changed into string.

# Input Function in Python:
print("Enter your name : ")
name = input() #It will take input from user
print("Your Name is",name) # It will show the name
xyz = input("Enter your age : ")
print("Your age is ",xyz)
