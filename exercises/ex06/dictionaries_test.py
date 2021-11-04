"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730398576"


def test_invert_normal() -> None:
    """Tests for normal invert scenario."""
    x: dict[str, str] = {"taylor": "swift"}
    assert invert(x) == {"swift": "taylor"}


def test_invert_error() -> None:
    """Test for same keys."""
    x: dict[str, str] = {"dog": "house", "tree": "house"}
    assert invert(x) == KeyError


def test_invert_more() -> None:
    """More tests for the invert function!"""
    x: dict[str, str] = {"harry": "styles", "niall": "horan", "zayn": "malik"}
    assert invert(x) == {"styles": "harry", "horan": "niall", "malik": "zayn"}


def test_favorite_color_normal() -> None:
    """Normal scenario for fav colors!"""
    x: dict[str, str] = {"Amina": "purple", "Julia": "blue", "Joe": "blue"}
    assert favorite_color(x) == "blue"


def test_favorite_color_many() -> None:
    """Test for when 2 colors are most frequent."""
    x: dict[str, str] = {"Harry": "yellow", "Niall": "yellow", "Zayn": "blue", "Louis": "blue"}
    assert favorite_color(x) == "yellow"


def test_favorite_color_one() -> None:
    """Only one favorite color!"""
    x: dict[str, str] = {"Amina": "purple", "Taylor": "purple"}
    assert favorite_color(x) == "purple"


def test_count_normal() -> None:
    """Normal scenario for count function."""
    x: list[str] = ["eggs", "bacon", "grits", "eggs", "bacon", "eggs"]
    assert count(x) == {"eggs": 3, "bacon": 2, "grits": 1}


def test_count_many() -> None:
    """When there is too many items, yikes!"""
    x: list[str] = ["bob", "yellow", "cat", "dog", "cat", "bob", "dog", "cat"]
    assert count(x) == {"bob": 2, "yellow": 1, "cat": 3, "dog": 2}


def test_count_five() -> None:
    """When one word appears five times!"""
    x: list[str] = ["hello", "world", "world", "hello", "hello", "hello", "hello"]
    assert count(x) == {"hello": 5, "world": 2}
