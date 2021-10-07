"""Repeating a beat in a loop."""

__author__ = "730398576"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
times: str = input("How many times do you want to repeat it? ")
x = int(times)
while x <= 0:
    print("No beat...")
    x += 1
    while x > 0:
        print(beat)
        x += 1