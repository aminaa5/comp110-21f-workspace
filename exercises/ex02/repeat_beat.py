"""Repeating a beat in a loop."""

__author__ = "730398576"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
x: str = ""
i: int = 0
if times <= 0:
    print("No beat...")
else:
    while i < times:
        if i < times - 1:
            x = x + beat + " "
        else:
            x = x + beat
        i += 1
times -= 1

print(x)