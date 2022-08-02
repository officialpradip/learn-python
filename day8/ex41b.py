# Override Explicity

class Parent(object):
    def override(self):
        print("This is parent")


class Child(Parent):
    def override(self):
        print("This is child")


mother = Parent()
daughter = Child()

mother.override()  # it runs override function from parent class
daughter.override()  # it runs override function from child class
