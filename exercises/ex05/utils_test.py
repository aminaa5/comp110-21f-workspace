"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
__author__ = "730398576"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_positive() -> None:
    """Tests for positve even."""
    x: list[int] = [2, 4, 6, 6, 6, 3, 2, 5, 7, 8, 7, 0]
    assert only_evens(x) == [2, 4, 6, 6, 6, 2, 8, 0]


def test_only_evens_negative() -> None:
    """Tests for negative even."""
    x: list[int] = [-2, 4, 2, 6, -1, 1]
    assert only_evens(x) == [-2, 4, 2, 6]


def test_only_evens_empty() -> None:
    """Tests for empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_sub_normal() -> None:
    """Tests for sub."""
    a: list[int] = [2, 3, 4, 6, 1, 4, 8, 2, 5]
    x: int = 3
    y: int = 7
    assert sub(a, x, y) == [6, 1, 4, 8]


def test_sub_negative() -> None:
    """Tests for negative start index."""
    a: list[int] = [3, 4, 2, 1, 3]
    x: int = 0
    y: int = 3
    assert sub(a, x, y) == [3, 4, 2]


def test_sub_empty() -> None:
    """Tests for empty list."""
    a: list[int] = []
    x: int = 2
    y: int = 4
    assert sub(a, x, y) == []


def test_concat_different() -> None:
    """Tests for different length lists."""
    x: list[int] = [2, 4, 3]
    y: list[int] = [2, 1]
    assert concat(x, y) == [2, 4, 3, 2, 1]


def test_concat_empty() -> None:
    """Tests for empty list."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_same() -> None:
    """Tests for same length lists."""
    x: list[int] = [2, 7, 4]
    y: list[int] = [3, 5, 6]
    assert concat(x, y) == [2, 7, 4, 3, 5, 6]