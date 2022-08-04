def show(a, b):
    while a <= b:
        yield a
        a += 1


result = show(5, 10)
print(result)
print(next(result))  # next() used to retrive elements
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
for i in result:
    print(i)
