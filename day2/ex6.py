#strings and text
from xmlrpc.client import boolean


people = "There are %d number of people" % 10
print(people)

country = "Nepal"
capital = "Kathmandu"
sentence = "%s is the capital city of country %s" % (capital, country)
print(sentence)

print("I said: %r" % people)
print("I said: '%s'" % people)


# %r for debugging where as %s %d are for displaying to users
# string concatenation
string_con = country + "" + capital
print(string_con)


string_con = country + "" + capital + str(10)  # int to str
print(string_con)


is_accepted = boolean(0)
print(is_accepted)
