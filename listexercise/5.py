"""
Write a program to display those items from a list that is divisible by 5
"""
num = [3, 5, 7, 9, 23, 15]
for i in num:
    if i % 5 == 0:
        print(i, end=" ")
    else:
        print("Not divisible by 5")
