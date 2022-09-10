# Regular Expression Operations
"""
1. Find a word in string
"""
import re

para = re.findall(
    "Python", "Python is an interpreted, Python is an object-oriented, Python is high-level programming language with dynamic semantics.")


for i in para:
    print(i)


"""
2. Generate an iterator
"""
demo = "Python is an interpreted and object oriented languages. Are you pythonist"

for i in re.finditer("Python", demo):  # iterator using finditer
    locTuple = i.span()  # span() returns both start and end indexes in a single tuple
    print(locTuple)  # print in tuple form

"""
3. Match words with a particular pattern
"""
demo1 = "Sat, cat, mat,rat"  # at is common
result = re.findall("[Scmr]at", demo1)  # matching words with scmr end with at

for i in result:
    print(i)

"""
4. Match series of range of characters
"""
demo2 = "Sat, cat, mat,rat"  # at is common
result = re.findall("[c-m]at", demo2)  # matching words with scmr end with at
# result = re.findall("[^c-m]at", demo2) get beyond c to m
for i in result:
    print(i)

print("---------------------"*2)
"""
5. replace a string
"""
demo3 = "Sat, cat, mat,rat"
regex = re.compile("[r]at")  # replacing rat with rabbit

result = regex.sub("rabbit", demo3)
print(result)

print("---------------------"*2)
"""
6. Match a single character
"""
demo4 = "1234567890"
matches = len(re.findall("\d(5)", demo4))  # \d placeholder for number
print(matches)
