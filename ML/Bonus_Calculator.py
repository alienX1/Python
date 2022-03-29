# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary: "))
service_year = int(input("Enter your service year: "))

if service_year < 5:
    print("You will not get any bonous. ")
    print("Your Salary: ", salary)
else:
    print("Here is your 5% bonus: ",salary*0.05)
    print("Your salary: ",salary + salary*0.05)
