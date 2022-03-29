Name = input("Enter your Name: ")
Age = int(input("Enter your age: "))
Gender = input("Gender (M/F): ")
Height = int(input("Enter your height: "))
Weight = int(input("Enter your weight: "))

# Body Mass Index
BMI = float(Weight / (Height**2) * 703)
print("Body Mass Index: ", BMI)

if BMI < 16:
    print(Name, ", you are severely Underweight.")
elif 16 <= BMI < 18.5:
    print(Name, 'you are Underweight.')
elif 18.5 <= BMI < 25:
    print(Name, 'you are Healthy.')
elif 25 <= BMI < 30:
    print(Name, 'you are Overweight.')
else: print(Name, 'you are Obese.')