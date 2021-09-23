"""Drawing forests in a loop."""

__author__ = "730398576"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
print("Depth: ")
line = 0
depth = int(input()) 
emoji = 1
while depth != line:
    print(TREE * emoji)
    line += 1 
    emoji += 1