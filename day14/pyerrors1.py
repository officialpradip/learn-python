# Python Exception Handling Using try, except and finally statement

# import module sys to get the type of exception
import sys

List = ['a', 0, 2]

for i in List:
    try:
        print("The entry is", i)
        r = 1/int(i)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", i, "is", r)
