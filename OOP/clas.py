class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

    def fullname(self):
        return f"{self.first}  {self.last}"


emp1 = Employee("Ram", "Karki", 100000)
# emp2 = Employee()

print(emp1.email)
print(emp1.fullname())
