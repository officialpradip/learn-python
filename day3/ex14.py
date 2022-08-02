# Reading files
from sys import argv

script, file = argv
f = open(file)  # opening files

print("Her's your file %s:" % file)
print(f.read())  # reading ex14_sample.txt files

print("Enter your file name again")
file_again = input()
f_again = open(file_again)
print(f_again.read())
