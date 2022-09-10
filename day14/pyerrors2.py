# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0  # assert keyword is used when debugging the code
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
