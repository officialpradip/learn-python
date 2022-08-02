# More Variables and Printing
from audioop import add


name = "Pradip"
age = 23
address = "Kathmandu"
print("Name is %s" % name)  # %s is used a placeholder for string values
print("Age is %d" % age)  # %d is used as placeholder for number or float values
print("Address is %s" % address)
print("Name is %s and address is %s" % (name, address))


print("Full bio is %s, %d,%s" % (name, age, address))

""" Note:%s and %d are formatters that take
the variable on the right and put it in to replace the %s with its value"""
