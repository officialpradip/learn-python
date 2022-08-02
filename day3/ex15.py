# Reading and writing files
"""
 • close —Closes the file. Like File
 • read —Reads the contents of the file
 • readline —Reads just one line of a text file.
 • truncate —Empties the file. 
 • write(stuff) —Writes stuff to the fi le.
"""
from sys import argv

current_script, filename = argv

print("Erasing the file %s:" % filename)
print("Hit CTRL- C (^C) to abort")
print("Hit ENTER to continue")

input("?")
print("Opening the file")
target = open(filename, 'w')

print("Truncating the file")
target.truncate()

print("Provide 3 different lines about yourself")

line1 = input("first line: ")
line2 = input("Second line: ")
line3 = input("third line: ")

print("Different three lines are saved on the file")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("File is closing")
target.close()


# run python ex15.py ex15test.py on command line
