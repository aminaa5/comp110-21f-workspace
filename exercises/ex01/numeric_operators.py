"""This exercises involves practicing numberic operators, type conversations, and string concatenation."""

__author__ = "730398576"


left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
i = int(left)
j = int(right)
a = (i ** j)
b = (i / j)
c = (i // j)
d = (i % j)
e = "is"
print(i, "**", j, e, a)
print(i, "/", j, e, b)
print(i, "//", j, e, c)
print(i, "%", j, e, d)
