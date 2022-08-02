# Alter Before or After

class Parent:

    def altered(self):
        print("Parent altering")


class Child(Parent):
    def altered(self):
        print("Child, before parent altering")
        # super() is used to give access to method
        super(Child, self).altered()  # get parent class
        print("Child, after parent altering")


father = Parent()
son = Child()

father.altered()
son.altered()
