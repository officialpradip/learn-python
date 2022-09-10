# passing lambda function to another function

def show(x):
    print(x(20))


show(lambda x: x+2)

# another


def add():
    y = 50
    return (lambda x: x+y)


a = add()  # function call
print(a(10))
