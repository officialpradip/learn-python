# Asking question i.e taking input

print("What is your name?")
ans = input()
print("Where are you from?")
address = input()
print("You are %s and you are from %s" % (ans, address))


# anotherway
name = input("What is your name?")
address = input("Where are you from?")
print("Your are", name, "and you are from", address)
print(f"You are {name} and you are from {address}")
