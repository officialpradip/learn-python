# first identify the patterns

import re

Nameage = """
Ram is 23 and Sam is 24
Shyam is 30 and Hari is 22
Krishna is 19
"""
ages = re.findall(r'\d{1,3}', Nameage)
print(ages)

names = re.findall(r'[A-Z][a-z]*', Nameage)
# [A-Z] name begins with capital letter
# [A-Z] name ends with small letter
# * represents all
print(names)

NameageDict = {}  # empty dictionery
x = 0
for eachname in names:
    NameageDict[eachname] = ages[x]
    # code split
    # NamgeageDict[eachname] get first names
    # ages[x] get first ages
    x += 1

print(NameageDict)
