"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730398576"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
a = str("You will find true love in two days! <3")
b = str("Take a break and watch good energy enter your life! :)")
c = str("Someone with purple hair will enter your life!! :P")
x = int(a)
y = int(b)
z = int(c)
if x == 1:
    print(a)
    if y == 2:
        print(b)
        if z == 3:
            print(c)
randint(1, 3)
print("Now, go spread positive vibes!")