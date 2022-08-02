#Numbers and Math

"""
+ plus     - minus     / slash      * asterisk     % percent
< less- than     > greater- than      <= less- than- equal
>= greater- than- equal 

Parentheses have the highest precedence and can be used 
to force an expression to evaluate in the order we want
 """


# usage of math for counting chickens
from xmlrpc.client import boolean


print("Hello there, I am counting chickens")

print("No of hens", (20+20) / 2)  # operation of () will be performed first


print(25*3 % 4)
print("Roosters", 100-25*3 % 4)  # 25*3%4 results in 3

print("Counting eggs:")
print(1/4)
print(4 % 2)  # remainder = 0
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)


print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print(2 == 2)  # equals
print(5 < -2)  # less than
print(-2 < 5)
print(5 > 5)  # greather than
print(5 >= 5)  # greater or equals

print("this is", boolean(1))  # true
print("this is", boolean(0))  # false
