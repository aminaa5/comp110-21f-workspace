"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
__author__ = "730398576"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    x: list[int] = [2, 4, 6, 6, 6, 3, 2, 5, 7, 8, 7, 0]
    assert only_evens(x) == [2, 4, 6, 6, 6, 2, 8, 0]


def test_sub() -> None:
    a: list[int] = [2, 3, 4, 6, 1, 4, 8, 2, 5]
    x: int = 3
    y: int = 7
    assert sub(a, x, y) == [6, 1, 4, 8]


def test_concat() -> None:
    x: list[int] = [2, 4, 3]
    y: list[int] = [2, 1]
    assert concat(x, y) == [2, 4, 3, 2, 1]