class Employee():
    growth = 1.2
    count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

        Employee.count += 1

    def fullname(self):
        return f"{self.first}  {self.last}"

    def increment(self):
        self.pay = self.pay*Employee.growth


emp1 = Employee("Ram", "Karki", 100000)
emp2 = Employee("Ram", "Karki", 100000)
# emp2 = Employee()
print(emp1.__dict__)
print(emp1.email)
print(emp1.fullname())
print(Employee.fullname)
print(Employee.fullname(emp1))
print(Employee.growth)
print(Employee.count)
