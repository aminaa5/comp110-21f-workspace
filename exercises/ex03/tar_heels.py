"""An exercise in remainders and boolean logic."""

__author__ = "730398576"


# Begin your solution here...
print("Enter an int: ")
number = int(input())
if number % 2 == 0 and number % 7 == 0:
    print("TAR HEELS")
elif number % 2 == 0:
    print("TAR")
elif number % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")