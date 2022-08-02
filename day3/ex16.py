# More files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s:" % (from_file, to_file))

in_file = open(from_file)
indata = in_file.read()
print(indata)

print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit ENTER to continue, CTRL- C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")
out_file.close()
in_file.close()


# RUN FILE ON COMMAND LINE USING python ex16.py ex15test.txt ex16test.txt
