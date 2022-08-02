#Names, Variables, Code and Functions
# function using def for “defi ne.”
def demo_print(*args):
    arg1, arg2 = args
    print("arg1 is %s and arg2 is %s" % (arg1, arg2))


demo_print("Hello", "How are you?")

# another way


def demo_print1(arg1, arg2):
    print("arg1 is %s and arg2 is %s" % (arg1, arg2))


demo_print1("Hello", "there!")

# one argument


def one(arg1):
    print("This is one arguments %s" % arg1)


print("Nepal")


def no_arg():
    print("this is no argument")


no_arg()
