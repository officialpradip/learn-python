# Making Decision

print("You are going into dark room. We have two rooms")
door = int(input("Enter either 1 or 2 to enter the room: "))

if door == 1:
    print("There's a gaint bear eating a cheese cake.")
    print("What do you want to do?")
    print("1. Take the cake.")
    print("2. Stare at the bear.")

    bear = int(input("Select your option: "))

    if bear == 1:
        print("Bear will attack you")
    elif bear == 2:
        print("Bear will enjoy the cake.")
    else:
        print("Bear runs away")
elif door == 2:
    print("You stare into the endless abyss at Cthulhu'sretina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = int(input("Select your option: "))
    if insanity == 1 or insanity == 2:
        print("Your body survives powered by a mind of jello.")
    else:
        print("The insanity rots your eyes into a pool of muck.")

else:
    print("Please select given options only")
