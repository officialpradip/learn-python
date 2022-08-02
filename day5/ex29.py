# while loops

i = 0
number = []

while i < 6:
    print(f"value of i is {i}")
    number.append(i)
    i += 1
    print("Number list is", number)

for num in number:
    print(num)


# student roll upto 10:
roll = 1
rollno = []
while roll <= 10:
    print(f"value of roll is {roll}")
    rollno.append(roll)
    roll += 1
    print("The rollno is", rollno)
