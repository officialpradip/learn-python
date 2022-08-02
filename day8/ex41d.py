class Parent:

    def override(self):
        print("Parent override")

    def implicit(self):
        print("Parent is implicit")

    def altered(self):
        print("Parent is altered")


class Child(Parent):

    def override(self):
        print("Child override")

    def altered(self):
        print("Child before Parent is altered")
        super(Child, self).altered()
        print("Child after Parent is altered")


dad = Parent()
son = Child()  # creating objects

dad.implicit()
son.implicit()  # taking from base class i.e parent
print("___________")
dad.override()
son.override()
print("___________")
dad.altered()
son.altered()
