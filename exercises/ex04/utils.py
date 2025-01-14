"""List utility functions."""

__author__ = "730398576"


# TODO: Implement your functions here.


def all(numbers: list[int], digit: int) -> bool:
    """Return True is all numbers in list equal the integer."""
    i: int = 0
    while i < len(numbers):
        if numbers == 0:
            return False
        if numbers[i] == digit:
            i += 1 
        else:
            return False
    return True


def is_equal(first: list[int], second: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    i: int = 0
    while i < len(first) and i < len(second):
        if len(first) != len(second):
            return False
        if first[i] == second[i]:
            i += 1 
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Return the largest value in the list."""
    i: int = 0
    max: int = input[0]
    while i < len(input):
        if len(input) == 0:
            raise ValueError("max() arg is an empty List")
        if input[i] > max:
            max = input[i]
            i += 1
        else:
            i += 1
    return max