# Composition
# has-a relationship
class Other(object):
    def override(self):
        print("OTHER overriding")

    def implicit(self):
        print("OTHER implicit")

    def altered(self):
        print("OTHER altered")


class Child(object):
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()  # accessing implicit() function from other class

    def override(self):
        print("Child override")

    def altered(self):
        print("Child before other altered")
        self.other.altered()
        print("Child after other  altered")


son = Child()

son.implicit()
son.override()
son.altered()

"""
Use composition to package code into modules that are used in many
different unrelated places and situations.

Use inheritance only when there are clearly related reusable pieces of code
that fit under a single common concept or if you have to because of
something you’re using.
"""
