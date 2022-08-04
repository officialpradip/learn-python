
def display(a, b):
    yield a
    yield b


result = display(100, 200)
print(result)
print(next(result))  # retrive data from generator object
print(next(result))
