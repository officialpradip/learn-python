"""
Exercise 2: Write a program to print all the elements of a list in single line.
"""
num = [23, 24, 54, 34, "hello"]

print("Count of items in num is:", len(num))
print(f"Reverse of {num} is: ", num[::-1])
for i in range(len(num)):
    print(num[i], end=" ")
