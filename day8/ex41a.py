# Inheritance versus Composition
# Implicit Inheritance
class Parent:
    def implicit(self):
        print("Parent implicit()")
        print("Just trying")


class Child(Parent):
    pass


dad = Parent()  # dad is object
son = Child()

dad.implicit()
son.implicit()

"""code demonestrate that if we put function in a base class
[ here Parent class is considered as base class]
then all subclasses [Child is considered as sub class] will 
automatically get base class features
"""
