"""Finding duplicate letters in a word."""

__author__ = "730398576"
print("Enter a word: ")
word: str = (input())
x: int = 0
doop: bool = False
while x < len(word):
    i: int = 0
    j: int = x + 1
    while i <= len(word):
        if word[x] != word[j]:
            i += 2
            j += 1
        else:
            print("Found duplicate: True")
        x += 1
        print("Found duplicate: False")