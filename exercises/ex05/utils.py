"""List utility functions part 2."""

__author__ = "730398576"


def only_evens(x: list[int]) -> list[int]:
    """Return only even numbers from list of numbers."""
    i: int = 0
    y: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1 
    return y


def sub(a: list[int], x: int, y: int) -> list[int]:
    """Given a start and end index, funtion will return a list between the start and end index."""
    b: list[int] = []
    if x < 0:
        x == 0
    if y > len(a):
        y == len(a)
    if len(a) == 0:
        return a
    while x < y:
        b.append(a[x])
        x += 1
    return b


def concat(x: list[int], y: list[int]) -> list[int]:
    """Return the first list followed by the second list."""
    i: int = 0 
    j: int = 0
    z: list[int] = []
    if len(x) == 0 and len(y) == 0:
        return z
    while i < len(x):
        z.append(x[i])
        i += 1
    while j < len(y):
        z.append(y[j])
        j += 1
    return z