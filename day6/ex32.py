# Doing Things to Lists

list = "Apple Mango Banana Orange Pee Pinepal Watermelon"
print("Above is not list. Let's make it list")

real_list = list.split(' ')  # split() function

more_list = ["Day", "Night", "Song", "Girl", "Boy"]

while len(real_list) != 10:
    next_one = more_list.pop()  # pop from last
    print("Adding: ", next_one)
    real_list.append(next_one)  # adding values from next_one to real_list
    print(f"There are {len(real_list)} items now.")

print("New list: ", real_list)  # displaying all list items

print("Playing with list.")

print(real_list[1])  # displaying items with index 1 i.e Mango
print(real_list[-1])  # displaying items from last i.e song
print(real_list.pop())  # removing last items from list i.e song
print('#'.join(real_list[3:5]))  # Orange#Pee
