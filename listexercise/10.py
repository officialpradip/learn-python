"Write a program to enter or append n numbers in a list."

num = []
n = int(input("How many number you want to add:"))
count = 0
for i in range(n):
    uin = int(input("Enter your number: "))
    count += 1
    num.append(i)
print(num)
