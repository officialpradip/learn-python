"""
Write a program to append data of the second list to the first list.
"""
list1 = [23, 24, 25, 26]
list2 = [27, 28, 29, 30]

# result = list1.append(list2)
# print(list1)
for i in range(len(list2)):
    list1.append(list2[i])

result = list1
print(result)
even = []
odd = []
for i in result:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
