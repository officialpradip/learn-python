#Loops and Lists

from xml.dom.minidom import Element


list = ['apple', 'banana', 'mango', 'orange', 'pinepal', 'grapes']
count = [1, 2, 3, 4, 5, 6, 7, 8]
change = [1, 'ktm', 2, 'pkr', 3, 'bkt']


for fruits in list:
    print(fruits)

for number in count:
    print("The count is", number)

for i in change:
    print("I got %s" % i)

# building list
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

# printing created list

for i in elements:
    print("Added element was", i)


# student roll no record

roll = []
for i in range(1, 10):
    print("Adding student roll no", i)
    roll.append(i)

for student in roll:
    print(f"student roll no was {student}")
