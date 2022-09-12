"""
Write a program in Python to remove duplicate items from a list.
"""

num = [2, 3, 4, 5, 2, 6, 3, 2]
no_dupli = []
for i in num:
    if i not in no_dupli:
        no_dupli.append(i)

print(no_dupli)
