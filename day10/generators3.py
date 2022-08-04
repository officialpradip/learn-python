import random


def lottery():
    for i in range(6):
        # can return any random number between 1 to 40
        yield random.randint(1, 40)


value = lottery()
print(value)
print(next(value))
for i in value:
    print(i)
