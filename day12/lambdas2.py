# normal function

def add(a, b):
    sum = a+b
    print("a+ b is", sum)


result = add(10, 12)

# lambda


def add(a, b): return a + b


print(add(10, 12))
print(add)


def add_sub(x, y): return (x+y, x-y)


a, s = add_sub(10, 5)
print(a)
print(s)
