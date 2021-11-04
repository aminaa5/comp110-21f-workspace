"""This exercise prints out demonstrations of relational operators."""

__author__ = "730398576"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")
i = int(left)
j = int(right)
a = "is"
b = bool(left < right)
c = bool(left >= right)
d = bool(left == right)
e = bool(left != right)
print(i, "<", j, a, b)
print(i, ">=", j, a, c)
print(i, "==", j, a, d)
print(i, "!=", j, a, e)