#Prompting and Passing

from sys import argv

script, username = argv


print("Hi %s, I'm the %s script." % (username, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % username)
likes = input()

print("Where do you live %s?" % username)
lives = input()

print("What kind of computer do you have?")
computer = input()

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))


# execute code by python ex13.py sam
