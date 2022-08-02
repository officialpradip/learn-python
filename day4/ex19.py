#Functions and Files

from sys import argv

script, file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)   # seek() function is used to change the position of the file handle


def print_line(line_count, f):
    print(line_count, f.readline())


current_file = open(file)

print("Let's print the file first")
print_all(current_file)

print("Let's rewind")
rewind(current_file)

print("Lets print three lines")

current_line = 1  # first line will be 1
print_line(current_line, current_file)

# second line will be 1 + 1 as current_line hold value 1
current_line = current_line + 1
print(current_line)
print_line(current_line, current_file)

# third line will be 2 + 1 as current line holdes value 2
current_line = current_line + 1
print_line(current_line, current_file)
