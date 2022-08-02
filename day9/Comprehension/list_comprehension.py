# List Comprehension
""""List comprehension represents the creation of new list from
an iterable object that satisfy a given condition
SYNTAX
new_list=[ expression for item in iterable_object if_statement]

List comprehension with if else statement
SYNTAX
new_list[i if i%==2 else "Invalid" for i in range(10)]
"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for i in list:
    new_list.append(i + 1)
print(new_list)

# above code to list comprehension
above_list = [i+1 for i in list]  # i +1 is expression
# element from list is taken out in i i.e is 1 then i+1 whill perform 1+1 i.e 2
print("this is above list", above_list)

list1 = [i for i in range(10)]
print("this is list without if statement", list1)

list2 = [i for i in range(10) if i % 2 == 0]
print("this is list with if_statement", list2)

list3 = [i for i in range(10) if i % 3 == 0]
print("this is list with if_statement", list3)

list4 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]
print("this is list with multiple if statement", list4)


# try
list = []
for i in range(20):
    if i % 2 == 0:
        list.append(i)  # i expression
print(list)


above_list_in_comprehension_form = [i for i in range(20) if i % 2 == 0]

# if else
list_if_else = []
for i in range(20):
    if i % 2 == 0:
        list_if_else.append(i)  # i expression
    else:
        list_if_else.append("INVALID")
print(list_if_else)

list_if_else_comprehension = [i if i %
                              2 == 0 else "INVALID" for i in range(20)]
print(list_if_else_comprehension)
