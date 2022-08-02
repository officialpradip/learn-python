# Printing Printing

formatter = "%r %r %r %r %r"
print(formatter % (1, 2, 3, 4, 5))
# print(formatter % ("one", "two", "three")) #error not enough arguments for format string
print(formatter % ("one", "two", "three", "four", "five"))
print(formatter % (formatter, formatter, formatter, formatter, formatter))

formatters = "{} {}"
print(formatters.format(1, 2))
