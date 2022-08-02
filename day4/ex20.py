# Functions can return something

def addition(num1, num2):
    print("Addition %d + %d" % (num1, num2))  # case of what function is doing
    return num1 + num2


def subtraction(num1, num2):
    print("Subtraction %d - %d" % (num1, num2))
    return num1 - num2


def multiply(num1, num2):
    print("Multiply %d * %d" % (num1, num2))
    return num1 * num2


def divide(num1, num2):
    print("Divide %d / %d" % (num1, num2))
    return num1 / num2


added_num = addition(20, 20)
subtract_num = subtraction(20, 10)
multiply_num = multiply(20, 10)
divide_num = divide(20, 10)


print("added_num:%d" % added_num)
print("subtract_num: %d" % subtract_num)
print("multiply_num: %d" % multiply_num)
print("divide_num: %d" % divide_num)
