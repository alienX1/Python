class Employee:
    company_code = 'alfa012'

    def __init__(self, age, name, eid):
        self.age = age
        self.name = name
        self.eid = eid

    def update(self):
        self.age = self.age + 1
        return self.age


E1 = Employee(24, 'Ravi', 101)
# print(type(E1))

print(E1.name)
# print(E1.company_code)
print(E1.age)
E1.update()
print(E1.age)


# Employee.company_code = 'seraPro02'
# print(E1.company_code)


class A:
    def __init__(self, x=1):
        self.x = x


class B(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y


def main():
    b = B()
    print(b.x, b.y)


main()
